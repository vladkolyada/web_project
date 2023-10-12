const path = require('path');

module.exports = {
  entry: {
    ind: './src/ind.js',
    about_sct: './src/about_sct.js',
    about_script_222: './src/about_script_222.js',
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  }
};