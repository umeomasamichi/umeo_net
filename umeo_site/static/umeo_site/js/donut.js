(function () {
    var blue = '#ddd';
    var gray = '#333';

    var data = {
        datasets: [{
            data: [99, 1],
            backgroundColor: [blue, gray],
            borderWidth: 0,
        }],
    };

    // グラフオプション
    var options = {
        // グラフの太さ（中央部分を何％切り取るか）
        cutoutPercentage: 85,
        // 凡例を表示しない
        legend: { display: false },
        // 自動サイズ変更をしない
        responsive: false,
        // タイトル
        title: {
            display: false,
            fontSize: 16,
            text: 'Progress',
        },
        
        // マウスオーバー時に情報を表示しない
        tooltips: { enabled: false },
    };

    // グラフ描画
    var ctx = document.getElementById('chart-area').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: options
    });
})();

(function () {
    var blue = '#ddd';
    var gray = '#333';

    var data = {
        datasets: [{
            data: [83, 17],
            backgroundColor: [blue, gray],
            borderWidth: 0,
        }],
    };

    // グラフオプション
    var options = {
        // グラフの太さ（中央部分を何％切り取るか）
        cutoutPercentage: 85,
        // 凡例を表示しない
        legend: { display: false },
        // 自動サイズ変更をしない
        responsive: false,
        // タイトル
        title: {
            display: false,
            fontSize: 16,
            text: 'Progress',
        },
        
        // マウスオーバー時に情報を表示しない
        tooltips: { enabled: false },
    };

    // グラフ描画
    var ctx = document.getElementById('chart-area2').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: options
    });
})();


(function () {
    var blue = '#ddd';
    var gray = '#333';

    var data = {
        datasets: [{
            data: [50, 50],
            backgroundColor: [blue, gray],
            borderWidth: 0,
        }],
    };

    // グラフオプション
    var options = {
        // グラフの太さ（中央部分を何％切り取るか）
        cutoutPercentage: 85,
        // 凡例を表示しない
        legend: { display: false },
        // 自動サイズ変更をしない
        responsive: false,
        // タイトル
        title: {
            display: false,
            fontSize: 16,
            text: 'Progress',
        },
        
        // マウスオーバー時に情報を表示しない
        tooltips: { enabled: false },
    };

    // グラフ描画
    var ctx = document.getElementById('chart-area3').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: options
    });
})();


var chartJsPluginCenterLabel = {
    afterDatasetsDraw: function (chart) {
        // ラベルの X 座標と Y 座標
        var canvas = chart.ctx.canvas;
        var labelX = canvas.clientWidth / 2;
        var labelY = Math.round((canvas.clientHeight + chart.chartArea.top) / 2);
        // ラベルの値
        var value = chart.data.datasets[0].data[0] + '%';
        // ラベル描画
        var ctx = this.setTextStyle(chart.ctx);
        ctx.fillText(value, labelX, labelY);
    },

    /**
      * 書式設定
      */
    setTextStyle: function (ctx) {
        var fontSize = 12;
        var fontStyle = 'normal';
        var fontFamily = '"Helvetica Neue", Helvetica, Arial, sans-serif';
        ctx.font = Chart.helpers.fontString(fontSize, fontStyle, fontFamily);
        ctx.fillStyle = '#ccc';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        return ctx;
    }
};

// 上記プラグインの有効化
Chart.plugins.register(chartJsPluginCenterLabel);