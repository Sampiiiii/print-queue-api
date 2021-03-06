const webpack = require('webpack');
const config = {
    entry:  __dirname + '/js/index.js',
    devtool: 'eval-source-map',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
  
    module: {
        rules: [
            {
            test: /\.(js|jsx)?/,
                exclude: /node_modules/,
                use: 'babel-loader'     
            }        
        ]
    }
};
module.exports = config;