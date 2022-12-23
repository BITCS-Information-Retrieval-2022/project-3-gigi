<template>
    <div class="abstract-text">
        <span 
            :style="{ 'max-height': status ? textHeight : '' }" 
            :class="{ statusText: status }" 
            class="titleText"
            ref="desc">
            {{ text }}
        </span>
        <span v-if="idShowText" 
            @click="status = !status" 
            :class="{ openSpan: status }" 
            class="openClose">
            {{ status ? "展开" : "收起" }}
        </span>
    </div>
</template>
<script>
export default {
    props: {
        rawText: {
            type: String,
            default: ""
        }
    },
    data() {
        return {
            text: this.rawText,
            //     "这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子这是一个测试的标题的例子，这是一个测试的标题的例子，这是一个测试的标题的例子",
            textHeight: null,
            status: false,
            idShowText: false
        };
    },
    mounted() {
        this.$nextTick(() => {
            setTimeout(() => {
                this.calculateText();
            }, 0);
        });
    },
    methods: {
        calculateText() {
            // 这是默认两行数据的高度，一行的高度可以自定义 可以*3 *4达到三行或者四行显示展示和收起的效果
            let twoHeight = 0.16 * 4.5;
            this.textHeight = `${twoHeight}rem`;
            let curHeight = this.$refs.desc.offsetHeight;
            // console.log("curHeight", curHeight);
            // console.log("twoHeight", twoHeight);
            if (curHeight > twoHeight) {
                this.status = true;
                this.idShowText = true;
            } else {
                this.status = false;
                this.idShowText = false;
            }
        }
    }
};
</script>
<style lang="less" scoped>
.abstract-text {
    position: relative;

    .titleText {
        color: #666;
        overflow: hidden;
        text-overflow: ellipsis;

        .highlight {
            color: rgb(255, 13, 13);
            font-weight: 400;
        }
    }

    .openClose {
        background-color: rgb(189, 67, 62);
        border-radius: 0.1rem;
        font-size: 0.13rem;
        padding: 0 0.05rem 0 0.05rem;
        font-weight: 400;
        color: rgb(255, 255, 255);
        cursor: pointer;
    }

    .openSpan {
        position: absolute;
        bottom: 0.03rem;
        right: 0;
        background-color: rgb(189, 67, 62);
        border-radius: 0.1rem;
        font-size: 0.13rem;
        padding: 0 0.05rem 0 0.05rem;
        font-weight: 400;
        color: rgb(255, 255, 255);
    }
    .beta {
			position: absolute;
			top: 0;
			left: 0.4rem;
			background-color: #2600ff;
			border-radius: 0.1rem;
			font-size: 0.13rem;
			padding: 0 0.05rem 0 0.05rem;
			font-weight: 900;
			color: rgb(255, 255, 255);
    }

    .statusText {
        // content: "  ";
        overflow: hidden;
        display: block;
    }

    .statusText:after {
        position: absolute;
        bottom: 0;
        right: 2px;
        width: 48px;
        padding-left: 30px;
    }
}
</style>