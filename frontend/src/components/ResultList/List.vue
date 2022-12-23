<template>
	<div class="list">
		<el-empty v-if="SearchResult.totalNums == 0" description="没有相关内容，试试其他关键词吧~" style="margin-top: 1.8rem">
		</el-empty>
		<div class="hit-list">
			<div class="hit-item" v-for="(item, i) in SearchResult.hitList" :key="i"
				:class="{ active: IsActive && current_index == i }" @mouseenter="(IsActive = true), (current_index = i)"
				@mouseleave="(IsActive = false), (current_index = -1)">
				<router-link :to="{ path: '/detail', query: {index: i, id: item.id} }">
					<div class="title" target="_blank" v-html="item.title"></div>
				</router-link>
				<div class="related">
					<a class="related-item" v-if="isValidURL(item.source_url)" target="_blank" style="cursor: pointer">
						<i class="iconfont icon-bank"></i>&nbsp;来源
					</a>
					<a class="related-item" v-if="isValidURL(item.pdf_url)" target="_blank" style="cursor: pointer">
						<i class="iconfont icon-file-pdf"></i>&nbsp;PDF
					</a>
					<a class="related-item" v-if="isValidURL(item.ebook_url)" target="_blank" style="cursor: pointer">
						<i class="iconfont icon-book"></i>&nbsp;电子书
					</a>
					<a class="related-item" v-if="isValidURL(item.ppt_url)" :href="item.ppt_url" target="_blank" style="cursor: pointer">
						<i class="iconfont icon-file-ppt"></i>&nbsp;PPT
					</a> 
					<a class="related-item" v-if="isValidURL(item.video_url)" target="_blank" style="cursor: pointer">
						<i class="iconfont icon-video1"></i>&nbsp;相关视频
					</a>
					<a class="related-item" v-if="item.citations_num > 0" target="_blank" style="cursor: pointer">
						<i class="iconfont icon-fire"></i>&nbsp;{{ item.citations_num }}
					</a>
				</div>
				<span class="yearText" style="color:green">
            		{{item.year}}-{{ item.volume }}
        		</span>
				<!-- <div class="content" v-html="item.abstract"></div> -->
				<abstract :rawText=item.abstract></abstract>
			</div>
		</div>
	</div>
</template>

<script>
// import store from "@/store/index.js";
import { mapState, mapMutations } from "vuex";
import Abstract from "@/components/ResultList/Abstract.vue";

export default {
	data() {
		return {
			IsActive: false,
			current_index: -1, // 找到当前卡片，避免全部高亮
			loading: false,
			svg: `
        <path class="path" d="
          M 30 15
          L 28 17
          M 25.61 25.61
          A 15 15, 0, 0, 1, 15 30
          A 15 15, 0, 1, 1, 27.99 7.5
          L 15 15
        " style="stroke-width: 4px; fill: rgba(0, 0, 0, 0)"/>
      `,
		};
	},
	props: ["hitList"],
	updated() {
		console.log("SearchResult: ", this.SearchResult);
	},
	computed: {
		...mapState(["SearchResult"]),
	},
	components: {
		Abstract,
	},
	methods: {
        isValidURL(url){
            return url !== null && url !== undefined && url !== '';
        }
    },
};
</script>

<style lang="less">
.list {
	min-height: 7rem;

	.hit-list {
		margin-left: 1.5rem;
		text-align: left;
		width: 8rem;
	}

	.hit-item {
		border-radius: 0.1rem;
		margin-top: 0.1rem;
		padding: 0.1rem 0.1rem 0.2rem 0.1rem;

		.title {
			font-size: 0.2rem;
			font-weight: 900;
			color: rgb(189, 67, 62);
			margin-bottom: 0.1rem;
		}
		
		a {
			text-decoration: none;
		}

		.related {
			margin-bottom: 0.1rem;

			.related-item {
				text-decoration: none;
				float: auto;
				padding: 0rem 0.2rem 0rem 0rem;
				color: rgb(0, 0, 0);
			}

			.related-item:hover {
				color: rgb(189, 67, 62);
				// text-decoration:underline;
			}
		}

		.content {
			color: #666;
			overflow: hidden;
			text-overflow: ellipsis;
			display: -webkit-box;
			-webkit-box-orient: vertical;
			-webkit-line-clamp: 3;

			.highlight {
				color: rgb(255, 13, 13);
				font-weight: 400;
			}
		}
	}

	.active {
		box-shadow: 0.05rem 0.05rem 0.1rem #999;
		background-color: #eee;
		transition: all 0.8s;
	}
}
</style>
