<template>
  <div id="center">
<!--    <div class="month-select">-->
<!--      <select v-model:="selectedYearMonth" @change="fetchdata">-->
<!--        <option-->
<!--          v-for="item in yearMonthOption"-->
<!--          :key="item"-->
<!--          :value="item"-->
<!--          :selected="item === selectedYearMonth"-->
<!--        >-->
<!--          {{ item }}-->
<!--        </option>-->
<!--      </select>-->
<!--    </div>-->
    <div class="up">
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 20px">本月销冠</p>
        <div style="text-align: center">
          {{this.result.most_popular_car}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 20px">销冠销量</p>
        <div style="text-align: center">
          {{this.result.most_popular_car_sales}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 20px">最受欢迎类别</p>
        <div style="text-align: center">
          {{this.result.max_car_type}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 20px">最受欢迎类别销量</p>
        <div style="text-align: center">
          {{this.result.max_car_type_count}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 20px">最受欢迎品牌</p>
        <div style="text-align: center">
          {{this.result.max_brand}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 20px">最受欢迎品牌销量</p>
        <div style="text-align: center">
          {{this.result.max_brand_count}}
        </div>
      </div>
    </div>
    <div class="down">
      <div class="ranking bg-color-black">
        <span>
          <icon name="chart-pie" class="text-icon"></icon>
        </span>
        <span class="fs-xl text mx-2 mb-1 pl-3" style="font-size: 20px">品牌风云榜</span>
        <dv-scroll-ranking-board class="dv-scr-rank-board mt-1" :config="ranking" v-bind:key="ranking.data[0].value" />
      </div>
      <div class="percent">
        <div class="item bg-color-black">
          <span>燃油占比</span>
          <CenterChart
            :id="rate[0].id"
            :tips="rate[0].tips"
            :colorObj="rate[0].colorData"
          />
        </div>
        <div class="item bg-color-black">
          <span>纯电占比</span>
          <CenterChart
            :id="rate[1].id"
            :tips="rate[1].tips"
            :colorObj="rate[1].colorData"
          />
        </div>
        <div class="water">
          <p>混动占比</p>
          <dv-water-level-pond class="dv-wa-le-po" :config="water" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CenterChart from '@/components/echart/center/centerChartRate'
export default {
  data() {
    // const currentYear = new Date().getFullYear()
    // const years = []
    // for (let i = 0; i < 3; i++) {
    //   years.push(currentYear - i)
    // }
    //
    // const months = []
    // for (let i = 1; i <= 12; i++) {
    //   months.push(i < 10 ? `0${i}` : i)
    // }
    //
    // const yearMonthOption = []
    // years.forEach(year => {
    //   months.forEach(month => {
    //     yearMonthOption.push(`${year}${month}`)
    //   })
    // })
    return {
      // yearMonthOption,
      // selectedYearMonth: `${currentYear}${new Date().getMonth() + 1 < 10 ? '0' : ''}${new Date().getMonth() + 1}`,
      result:'',
      ranking: {
        data: [],
        carousel: 'single',
        unit: '辆',
      },
      water: {
        data: [24, 45],
        shape: 'roundRect',
        formatter: '{value}%',
        waveNum: 3
      },
      // 通过率和达标率的组件复用数据
      rate: [
        {
          id: 'centerRate1',
          tips: 60,
          colorData: {
            textStyle: '#3fc0fb',
            series: {
              color: ['#00bcd44a', 'transparent'],
              dataColor: {
                normal: '#03a9f4',
                shadowColor: '#97e2f5'
              }
            }
          }
        },
        {
          id: 'centerRate2',
          tips: 40,
          colorData: {
            textStyle: '#67e0e3',
            series: {
              color: ['#faf3a378', 'transparent'],
              dataColor: {
                normal: '#ff9800',
                shadowColor: '#fcebad'
              }
            }
          }
        }
      ]
    }
  },
  components: {
    CenterChart
  },
  async mounted() {
    const res = await this.$http.get('/sales/center')
    this.result = res.data
    this.$set(this.ranking, 'data', res.data.roll_list)
    this.$set(this.rate[0], 'tips', res.data.oil_rate)
    this.$set(this.rate[1], 'tips', res.data.electric_rate)
    this.$set(this.water, 'data', [res.data.hybrid_rate])
    console.log(res)
  }
}
</script>

<style lang="scss" scoped>
#center {
  display: flex;
  flex-direction: column;
  .up {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    .item {
      border-radius: 6px;
      padding-top: 8px;
      margin-top: 8px;
      width: 32%;
      height: 70px;
      .dv-dig-flop {
        width: 150px;
        height: 30px;
      }
    }
  }
  .down {
    padding: 6px 4px;
    padding-bottom: 0;
    width: 100%;
    display: flex;
    height: 255px;
    justify-content: space-between;
    .bg-color-black {
      border-radius: 5px;
    }
    .ranking {
      padding: 10px;
      width: 59%;
      .dv-scr-rank-board {
        height: 225px;
      }
    }
    .percent {
      width: 40%;
      display: flex;
      flex-wrap: wrap;
      .item {
        width: 50%;
        height: 120px;
        span {
          margin-top: 8px;
          font-size: 14px;
          display: flex;
          justify-content: center;
        }
      }
      .water {
        width: 100%;
        .dv-wa-le-po {
          height: 120px;
        }
      }
    }
  }
}
</style>
