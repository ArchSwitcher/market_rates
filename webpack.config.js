const path = require('path')

module.exports = {
    entry: "./market_rates/frontend/src/index.js",
    module:{
        rules:[
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    },
    output: {
        path: path.resolve(__dirname, 'market_rates/frontend/static/frontend/' )
    }
}