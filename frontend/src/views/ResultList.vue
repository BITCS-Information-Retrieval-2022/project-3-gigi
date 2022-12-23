<template>
	<div class="result-list">
		<detail-nav></detail-nav>
		<div class="list-items">
			<some-tips></some-tips>
			<list></list>
			<el-backtop />
			<page-index></page-index>
		</div>
	</div>
</template>

<script>
import DetailNav from "@/components/ResultList/DetailNav.vue";
import SomeTips from "@/components/ResultList/SomeTips.vue";
import List from "@/components/ResultList/List.vue";
import PageIndex from "@/components/ResultList/PageIndex.vue";

import { reactive } from "vue";

export default {
	name: "ResultList",
	components: {
		DetailNav,
		SomeTips,
		List,
		PageIndex,
	},

	setup(props) {
		let state = reactive({
			hitList: [],
			page: 0,
			pageNums: 0,
			searchCostTime: 0,
			totalNums: 0,
		});
		return {
			state,
		};
	},
};
</script>
<style lang="less" scoped>
hr {
	margin-top: 0.5rem;
}
.list-items{
	position: absolute;
	top: 60px;
}
</style>
