module.exports = {
  publicPath: '/',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000/',
        secure: false,
        chagneOrigin: true
      },
      '/static/posters': {
        target: 'http://localhost:',
        secure: false
      },
    }
  }
}
