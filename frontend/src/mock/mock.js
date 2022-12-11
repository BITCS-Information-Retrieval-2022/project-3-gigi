/*
 * @File    :  /project-3-gigi/frontend/src/mock/mock.js
 * @Author  :  xuzf
 * @Contact :  xuzhengfei-email@qq.com
 * @Create  :  2022-11-12 10:54:23
 * @Update  :  2022-12-11 12:25:17
 * @Desc    :  None
 */
//引入mockjs
import { mock } from 'mockjs';   //安装的mockjs，并不是创建的mock.js

//使用mockjs模拟数据
mock(RegExp('http://mock/api/search' + '.*'), 'get', function () { //当post或get请求到/api/data路由时Mock会拦截请求并返回上面的数据
    let hitList_new = [
        {
            id: "1",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 1",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 31,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "2",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 2",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 0,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "3",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 3",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: null,
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 31,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "4",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 4",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 12,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "5",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 5",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 31,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "6",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 6",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 12,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "7",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 7",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 31,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "8",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 8",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 12,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "9",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 9",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 31,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        },
        {
            id: "10",
            title: "Multiplex Graph Neural Network for Extractive Text Summarization 10",
            authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
            abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
            doi: "10.18653/v1/2021.emnlp-main.11",
            year: 2021,
            month: 11,
            type: "Conference",
            venue: "EMNLP",
            volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
            source_url: "https://aclanthology.org/2021.emnlp-main.11/",
            pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
            ppt_url: "https://www.slideserve.com/vera/text-summarization",
            video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
            citations_num: 12,         // 被引次数
            // reference_list: [ref1, ref2, ...]     // 参考文献列表
        }
    ];
    let hitList = [
        {
            page_url: "www.baidu.com",
            title: "百度",
            content: "后来加了参数，mockjs好像不能识别了，返回404.这个该怎么解决，真的不能加参数吗，但是我总感觉这个不太对"
        },
        {
            page_url: "www.baidu.com",
            title: "百度",
            content: "后来加了参数，mockjs好像不能识别了，返回404.这个该怎么解决，真的不能加参数吗，但是我总感觉这个不太对"
        }
    ]
    
    return {
        page: 1,                                   // 当前第几页（从1开始）
        searchCostTime: 0.01, // 搜索用时（单位为秒）
        totalNums: 10,
        pageNums: 1,
        hitList: hitList_new
    }
})

mock(RegExp('http://mock/api/detail' + '.*'), 'get', function () {
    console.log("sdasdasdasdasdadadasda!!!!!!!!")
    let detail = {
        id: "1",
        title: "Multiplex Graph Neural Network for Extractive Text Summarization",
        authors: ["Baoyu Jing", "Zeyu You", "Tao Yang", "Wei Fan", "Hanghang Tong"],
        abstract: "Extractive text summarization aims at extracting the most representative sentences from a given document as its summary. To extract a good summary from a long text document, sentence embedding plays an important role. Recent studies have leveraged graph neural networks to capture the inter-sentential relationship (e.g., the discourse graph) within the documents to learn contextual sentence embedding. However, those approaches neither consider multiple types of inter-sentential relationships (e.g., semantic similarity and natural connection relationships), nor model intra-sentential relationships (e.g, semantic similarity and syntactic relationship among words). To address these problems, we propose a novel Multiplex Graph Convolutional Network (Multi-GCN) to jointly model different types of relationships among sentences and words. Based on Multi-GCN, we propose a Multiplex Graph Summarization (Multi-GraS) model for extractive text summarization. Finally, we evaluate the proposed models on the CNN/DailyMail benchmark dataset to demonstrate effectiveness of our method.",
        doi: "10.18653/v1/2021.emnlp-main.11",
        year: 2021,
        month: 11,
        type: "Conference",
        venue: "EMNLP",
        volume: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
        source_url: "https://aclanthology.org/2021.emnlp-main.11/",
        pdf_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
        ebook_url: "https://aclanthology.org/2021.emnlp-main.11.pdf",
        ppt_url: "https://www.slideserve.com/vera/text-summarization",
        video_url: "https://aclanthology.org/2021.emnlp-main.11.mp4",
        citations_num: 31,         // 被引次数
        reference_list: [          // 参考文献列表
            {id: 0, title: "Multiplex Graph Neural Network for Extractive Text Summarization", year: "2021"}, 
            {id: 4, title: "Multiplex Graph Neural Network for Extractive Text Summarization", year: "2021"}, 
            {id: 5, title: "Multiplex Graph Neural Network for Extractive Text Summarization", year: "2021"}]     
    }
    return detail
})

// //使用mockjs模拟数据
// mock('http://mock/api/headimage', 'get', function () {//当post或get请求到/api/data路由时Mock会拦截请求并返回上面的数据
//     let imgUrl = ['http://122.114.62.128:8003/Images/banner0.png', 'http://122.114.62.128:8003/Images/banner1.png']

//     return {
//         data: imgUrl
//     }
// })