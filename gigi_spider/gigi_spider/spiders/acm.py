import scrapy
import random
import time
import re
import pdb


class ACMSpider(scrapy.Spider):
    name = 'acm'

    acm_prefix = 'https://dl.acm.org'
    scihub_prefix = 'https://sci-hub.st'
    slideserve_prefix = 'https://www.slideserve.com'

    month_dict = {
        'January': '1', 'February': '2', 'March': '3',
        'April': '4', 'May': '5', 'June': '6',
        'July': '7', 'August': '8', 'September': '9',
        'October': '10', 'November': '11', 'December': '12'
    }
    slideserve_replace_dict = {
        ' ': '-', '+': '%2B', '&': '%26', '=': '%3D',
        '<': '%3C', '>': '%3E', '\"': '%22', '#': '%23',
        ',': '%2C', '%': '%25', '{': '%7B', '}': '%7D',
        '|': '%7C', '\\': '%5C', '^': '%5E', '~': '%7E',
        '[': '%5B', ']': '%5D', '`': '%60', ';': '%3B',
        '/': '%2F', '?': '%3F', ':': '%3A', '@': '%40',
        '$': '%24',
    }
    url_src_pth = 'gigi_spider/List/acm_url_list.txt'

    url_done_paper_pth = 'gigi_spider/List/done_paper.txt'
    url_done_page_pth = 'gigi_spider/List/done_page.txt'
    url_done_split_pth = 'gigi_spider/List/done_split.txt'

    debug_flag = True

    url_done_list = []
    url_done_page_list = []
    url_done_split_list = []

    def start_requests(self):
        with open(self.url_done_paper_pth, 'r', encoding='utf-8') as f:
            self.url_done_list = f.read().splitlines()
        with open(self.url_done_page_pth, 'r', encoding='utf-8') as f:
            self.url_done_page_list = f.read().splitlines()
        with open(self.url_done_split_pth, 'r', encoding='utf-8') as f:
            self.url_done_split_list = f.read().splitlines()

        urls = []
        with open(self.url_src_pth, 'r', encoding='utf-8') as f:
            urls = f.read().splitlines()
        random.shuffle(urls)
        for url in urls:
            if url in self.url_done_split_list:
                self.log(f"区间{url}爬过了，本次跳过。\n")
                continue
            wait = random.randint(1, 10)
            time.sleep(wait * 0.1)
            yield scrapy.Request(
                url=url, callback=self.parse, dont_filter=True)
        yield scrapy.Request(
            url=url, callback=self.parse_paper_homepage, dont_filter=True
        )

    def parse(self, response):
        paper_items = response.css('div.issue-item__content-right')
        if response.url not in self.url_done_page_list:
            for paper_item in paper_items:
                wait = random.randint(1, 10)
                time.sleep(wait * 0.1)
                try:
                    paper_url = self.acm_prefix + paper_item.css('span.hlFld-Title a').attrib['href']
                    if paper_url not in self.url_done_list:
                        yield scrapy.Request(
                            paper_url,
                            callback=self.parse_paper_homepage,
                            dont_filter=True)
                    else:
                        self.log(f"论文{paper_url}爬过了，本次跳过。\n")
                except Exception:
                    continue
            with open(self.url_done_page_pth, 'a') as f:
                f.write(response.url + '\n')
        else:
            self.log(f"页面{response.url}爬过了，本次跳过。\n")

        # 爬取下一页论文列表
        if len(paper_items) != 0:
            try:
                next_page = response.css('a.pagination__btn--next').attrib['href']
                if next_page is not None and self.debug_flag is True:
                    # self.debug_flag = False
                    yield scrapy.Request(
                        next_page, callback=self.parse, dont_filter=True)
            except Exception:
                pass
        else:
            with open(self.url_done_split_pth, 'a') as f:
                ori_url = re.sub('startPage=[0-9]+', 'startPage=0', response.url)
                f.write(ori_url + '\n')

    def parse_paper_homepage(self, response):
        # 获取breadcrumb信息，判断是否为会议期刊论文，如果是获取类型，如果不是不收集数据
        paper_type_url = response.css(
            'nav.article__breadcrumbs.separator a')[1].attrib['href']
        paper_type = paper_type_url[1:-1]
        # if paper_type_url == '/journals' or paper_type_url == '/conferences':
        #     paper_type = paper_type_url[1:-1]
        # else:
        #     with open('breaklunch/List/acm_done.txt', 'a') as f:
        #         f.write(response.url + '\n')
        #     return

        # 获取title, abstract, authors, doi和url
        title = response.css('h1.citation__title::text').get()
        abstract = response.css(
            'div.abstractSection.abstractInFull p::text').get()
        authors = response.css(
            'span.loa__author-name span::text').getall()
        # doi = response.css('a.issue-item__doi').attrib['href']
        url = response.url
        doi = url.replace(
            'dl.acm.org/doi', 'doi.org')

        # 获取时间
        date = response.css(
            'span.CitationCoverDate::text').get().split(' ')
        year = date[2]
        month = self.month_dict[date[1]]

        # 获取来源
        venue = response.css(
            'nav.article__breadcrumbs.separator a')[2].attrib['href']

        # 获取volume
        volume = response.css(
            'nav.article__breadcrumbs.separator a')[3].attrib['href']

        # 获取视频相关信息
        video_element = response.css(
            'div.article-media__item.separated-block--dashed--bottom.clearfix')
        if video_element is not None:
            try:
                video_postfix = video_element.css(
                    'div.video__links.table__cell-view a')[1].attrib['href']
                video_url = self.acm_prefix + video_postfix
            except Exception:
                video_url = ''
            try:
                thumbnail_path = video_element.css(
                    'stream.cloudflare-stream-player').attrib['poster']
            except Exception:
                thumbnail_path = ''
        else:
            video_url = ''
            thumbnail_path = ''

        # 获取引用信息
        in_citations = response.css(
            'span.citation span:nth-child(2)::text').get().replace(',', '')
        citations_num = int(in_citations)

        out_citations_list = response.css(
            'ol.rlist.references__list.references__numeric li')
        if len(out_citations_list) == 0:
            out_citations_list = response.css(
                'ol.rlist.references__list li')
        if out_citations_list is not None:
            out_citations = str(len(out_citations_list))
        else:
            out_citations = str(0)
        out_citations = out_citations
        reference_list = out_citations_list.css('.references__note::text').getall()

        # 获取pdf、ppt相关信息
        ret = {
            'title': title,
            'abstract': abstract,
            'authors': authors,
            'doi': doi,
            'year': year,
            'month': month,
            'type': paper_type,
            'venue': venue,
            'source_url': url,
            'pdf_url': '',
            'video_url': video_url,
            'thumbnail_path': thumbnail_path,
            'volume': volume,
            'ebook_url': '',
            'ppt_url': '',
            'citations_num': citations_num,
            'reference_list': reference_list}
        try:
            pdf_red_button = response.css('a.btn.red')
            pdf_url = self.acm_prefix + pdf_red_button.attrib['href']
            ret['pdf_url'] = pdf_url
            yield ret
        except KeyError:
            try:
                scihub_url = self.scihub_prefix + doi.split('doi.org')[-1]
                yield scrapy.Request(
                    scihub_url,
                    meta=ret,
                    callback=self.parse_scihub,
                    dont_filter=True)
            except Exception:
                yield ret

        # 爬完的页写入文档，以实现断点续爬
        with open(self.url_done_paper_pth, 'a') as f:
            f.write(response.url + '\n')

    def parse_scihub(self, response):
        try:
            scihub_suffix = response.xpath('//*[@id="buttons"]/button/@onclick').get().split('location.href=')[-1][1:-1]
            pdf_url = self.scihub_prefix + scihub_suffix
        except Exception:
            pdf_url = ''
        ret = response.meta
        ret['pdf_url'] = pdf_url

        year = int(ret['year'])
        if year >= 2012:
            title = ret['title']
            title_fmt = title.replace('%', '%25')
            for k, v in self.slideserve_replace_dict.items():
                title_fmt = title_fmt.replace(k, v)
            slideserve_url = self.slideserve_prefix + '/search/presentations/' + title_fmt
            yield scrapy.Request(
                slideserve_url,
                meta=ret,
                callback=self.parse_slideserve,
                dont_filter=True)
        else:
            yield ret

    def parse_slideserve(self, response):
        ret = response.meta
        try:
            # pdb.set_trace()
            slideserve_suffix = response.xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[1]/a/@href').get()
            ppt_url = self.slideserve_prefix + slideserve_suffix
            ret['ppt_url'] = ppt_url
        except Exception:
            ret['ppt_url'] = ''
        yield ret
