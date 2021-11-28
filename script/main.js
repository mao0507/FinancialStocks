var vm = new Vue({
    el: '#app',
    data: {
        stock: '',
        message: '110/11/27 UPDATE ',
        月領: '20000',
        年領: '',
    },
    mounted() {
        this.getStock();
    },
    computed: {
        countYear() {
            this['年領'] = this['月領'] * 12
            return this['年領']
        }
    },
    methods: {
        //取得股票資訊
        getStock() {
            let local = (window.location.href)
            let path
            if (local.indexOf('localhost') == -1) {
                path = 'json/data.json'
            } else {
                path = '/json/data.json'
            }


            this.stock = Mao.tools.get(path)
            if (this.stock != '' || this.stock == undefined) {
                console.log('data get work')
                    //console.log(this.stock)
            }
        },
        //計算需要張數
        countSheet(現金股利, 收盤股價, 股票股利) {
            this['年領'] = this['月領'] * 12
            let sheet = Mao.tools.roundToTwo(this['年領'] / ((現金股利 * 1000) + (收盤股價 * 股票股利 * 100)))
            return sheet
        },
        //計算需要多少錢
        countMoney(現金股利, 收盤股價, 股票股利) {
            this['年領'] = this['月領'] * 12
            let sheet = Mao.tools.roundToTwo(this['年領'] / ((現金股利 * 1000) + (收盤股價 * 股票股利 * 100)))


            let money = Mao.tools.thousandComma(Math.round(sheet * 收盤股價 * 1000))
            return money
        },
        //測試用
        test() {
            console.log('work')
        }
    }

})