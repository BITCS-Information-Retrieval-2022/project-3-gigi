<template>
	<div class="detail-nav">
		<router-link :to="{ path: '/' }">
			<div class="logo">
				Gigi
				<div class="beta">scholar</div>
			</div>
		</router-link>
		<div class="search">
			<search-box-detail></search-box-detail>
		</div>
		<div class="right">
			<router-link :to="{ path: '/' }">
				<svg class="icon" aria-hidden="true">
					<use xlink:href="#icon-yingyong"></use>
				</svg>
			</router-link>
			<!-- <svg class="icon" aria-hidden="true" @click="gomore">
				<use xlink:href="#icon-yingyongchengxu"></use>
			</svg> -->
		</div>
	</div>
</template>
<script>
import SearchBoxDetail from "@/components/ResultList/SearchBoxDetail.vue";

export default {
	components: {
		SearchBoxDetail,
	},
};
</script>

<style lang="less" scoped>
a {
	text-decoration: none;
	color: #000;
}
.router-link-active {
	text-decoration: none;
	color: #000;
}

.detail-nav {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 0.1rem 0.15rem 0.1rem 0.2rem;
	border-bottom: 1px solid #999;
	border-bottom: 0px;
	position: sticky;
	position: -webkit-sticky; // 兼容 -webkit 内核的浏览器
	top: 0px;
	// background-color: #ccc;
	background-color: rgb(189, 67, 62);
	.logo {
		font-size: 0.3rem;
		font-weight: 900;
		font-style: italic;
		position: relative;
		.beta {
			position: absolute;
			top: 0;
			left: 0.4rem;
			// background-color: rgb(255, 102, 14);
			background-color: #2600ff;
			border-radius: 0.1rem;
			font-size: 0.13rem;
			padding: 0 0.05rem 0 0.05rem;
			font-weight: 900;
			color: rgb(255, 255, 255);
		}
	}
	.search {
		position: absolute;
		top: 0.1rem;
		left: 1.2rem;
	}
	.right {
		display: flex;
		justify-content: space-around;
		align-items: center;
		.icon {
			width: 0.25rem;
			height: 0.25rem;
			fill: #222;
			margin-right: 0.2rem;
		}
		.ava {
			height: 0.4rem;
			height: 0.4rem;
			border-radius: 0.4rem;
			cursor: pointer;
		}
		.btn1 {
			font-size: 0.15rem;
			margin-right: 0.05rem;
			font-weight: 900;
		}
		.btn2 {
			font-size: 0.15rem;
			margin-left: 0.05rem;
			font-weight: 900;
		}
	}
}
</style>
