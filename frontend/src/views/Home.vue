<template>
	<div class="home">
		<logo></logo>
		<search-box></search-box>
		<page-footer></page-footer>
	</div>
</template>

<script>
// @ is an alias to /src
// import SampleNav from "@/components/Home/SampleNav.vue";
import Logo from "@/components/Home/Logo.vue";
import SearchBox from "@/components/Home/SearchBox.vue";
import PageFooter from "@/components/PageFooter.vue"

export default {
	name: "Home",
	components: {
		Logo,
		SearchBox,
		PageFooter
	},
};
</script>

<style lang="less" scoped>
// .home {
// }
</style>
