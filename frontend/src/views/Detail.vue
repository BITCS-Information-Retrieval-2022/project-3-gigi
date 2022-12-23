<template>
    <!-- <detail-nav></detail-nav> -->
    <div class="detail">
        <div class="source">
            <div> <b>Year:</b> {{ item.year }} </div>
            <div> <b>Volume:</b> {{ item.volume }} </div>
            <a v-if="isValidURL(item.source_url)" :href="item.source_url" ><b>Doi:</b> {{ item.doi }} </a>
        </div>
        <div class="title">
            <h1 v-html="item.title"></h1>
        </div>
        <div class="authors">
            <div class="author" v-for="(author, index) in item.authors" :key="index"> {{ author }}, </div>
        </div>
        <div class="related">
            <a class="related-item" v-if="isValidURL(item.source_url)" :href="item.source_url" target="_blank">
                <i class="iconfont icon-bank"></i>&nbsp;来源
            </a>
            <a class="related-item" v-if="isValidURL(item.pdf_url)" :href="item.pdf_url" target="_blank">
                <i class="iconfont icon-file-pdf"></i>&nbsp;PDF
            </a>
            <a class="related-item" v-if="isValidURL(item.ebook_url)" :href="item.ebook_url" target="_blank">
                <i class="iconfont icon-book"></i>&nbsp;电子书
            </a>
            <a class="related-item" v-if="isValidURL(item.ppt_url)" :href="item.ppt_url" target="_blank">
                <i class="iconfont icon-file-ppt"></i>&nbsp;PPT
            </a>
            <a class="related-item" v-if="isValidURL(item.video_url)" :href="item.video_url" target="_blank">
                <i class="iconfont icon-video1"></i>&nbsp;相关视频
            </a>
            <a class="related-item" v-if="item.citations_num > 0" target="_blank">
                <i class="iconfont icon-fire"></i>&nbsp;{{ item.citations_num }}
            </a>
        </div>
        <hr />
        <h2>摘要</h2>
        <div class="abstract" v-html="item.abstract"></div>
        <hr />
        <!-- <h2>相关视频</h2>
        <div class="related-video" :href="item.video_url" target="_blank">
            <video controls>
                <source :src="item.video_url" type="video/*">
                Download the <a href="item.video_url">video</a>.
            </video>
        </div>
        <hr /> -->
        <h2>参考文献</h2>
        <div class="references">
            <div v-for="(reference, index) in item.reference_list" :key="index">
                <!-- <div class="reference-index">{{ index + 1 }}.</div> -->
                <!-- <router-link :to="{ path: '/detail', query: {index: i, id: reference.id} }"> -->
                    <div class="reference-title" target="_blank" v-html="index + 1 + '. ' + reference.title"></div>
				<!-- </router-link> -->
            </div>
        </div>
        <PageFooter></PageFooter>
	</div>

</template>

<script>
// import { mapState } from "vuex";
import { useRoute } from "vue-router";
// import store from "@/store/index.js";
import { getDetail } from "@/api/index.js";

import DetailNav from "@/components/ResultList/DetailNav.vue";
import Abstract from "@/components/ResultList/Abstract.vue";
import PageFooter from "@/components/PageFooter.vue";

export default {
    name: "Detail",
    data() {
        return {
            item: {},
        };
    },
    async created() {
        const route = useRoute();
        console.log("Detail created");
        let id = route.query.id;
        console.log(id);
        console.log("loading");
        let that = this;
        let res = await getDetail(id);
        // store.commit("SetDetailResult", res.data);
        that.item = res.data;
        console.log("item:", this.item);
    },
    components: {
        DetailNav,
        Abstract,
        PageFooter,
    },
    methods: {
        isValidURL(url){
            return url !== null && url !== undefined && url !== '';
        }
    }
};
</script>

<style lang="less">
a {
    text-decoration: none;
    color: rgb(0, 0, 0);
}
.detail {
    margin-left: 1.5rem;
    margin-right: 1.5rem;
    text-align: left;    

    .source {
        margin-top: 0.2rem;
        margin-bottom: 0.15rem;
        font-size: 0.18rem;
        color: rgb(0, 0, 0);
    }

    .title {
        // h1 居中
        text-align: center;
    }
    
    .authors {
        margin-top: 0.15rem;
        margin-bottom: 0.15rem;
        text-align: center;

        .author {
            float: auto;
            display: inline;
            font-size: 0.2rem;
            padding: 0rem 0.1rem 0rem 0rem;
            color: rgb(0, 0, 0);
        }
    }

    .related {
        margin-bottom: 0.15rem;
        text-align: center;

        .related-item {
            text-decoration: none;
            float: auto;
            font-size: 0.15rem;
            padding: 0rem 0.2rem 0rem 0rem;
            color: rgb(0, 0, 0);
        }
    
        .related-item:hover {
            color: rgb(189, 67, 62);
            font-weight: 500;
        }
    }

    hr {
        margin-top: 0.15rem;
        margin-bottom: 0.15rem;
        border: 0;
        border-top: 1px solid #999;
    }

    .abstract {
        margin-top: 0.15rem;
        margin-bottom: 0.15rem;
        font-size: 0.2rem;
        color: rgb(0, 0, 0);
    }

    .related-video {
        margin-top: 0.15rem;
        margin-bottom: 0.15rem;
        text-align: center;
        video {
            width: 80%;
        }
    }

    .references {
        margin-top: 0.15rem;
        margin-bottom: 0.15rem;
        font-size: 0.2rem;
        color: rgb(0, 0, 0);
        float: left;

        .reference-index {
            float: left;
            text-align: right;
            padding-right: 0.1rem;
        }

        .reference-title {
            float: left;
            text-align: left;
            padding-left: 0.1rem;
        }

        .reference-year {
            float: left;
            text-align: left;
            padding-left: 0.1rem;
        }
    }
}

</style>