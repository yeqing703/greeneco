//导航轮播
banner()
function banner() {
  let top = document.querySelector('.top')
  let swiper = top.querySelector('.swiper_shop')
  let first = swiper.querySelector('li:first-of-type')
  let last = swiper.querySelector('li:last-of-type')
  swiper.appendChild(first.cloneNode(true))
  swiper.insertBefore(last.cloneNode(true), first)
  let lis = top.querySelectorAll('li')
  let len = lis.length
  let w = top.offsetWidth
  // must
  swiper.style.width = len * w + 'px'
  for (let i = 0; i < len; i++) {
    lis[i].style.width = w + 'px'
  }
  // 
  let ind = 1
  swiper.style.left = -ind * w + 'px'
  let inter = setInterval(function () {
    ind++
    swiper.style.transition = "left 0.5s ease-in-out"
    swiper.style.left = -ind * w + 'px'
    setTimeout(function () {
      if (ind == len - 1) {
        ind = 1
        swiper.style.transition = "none"
        swiper.style.left = -ind * w + 'px'
      }
    }, 500)
  }, 2000)
}

document.addEventListener('DOMContentLoaded', () => {
    // 初始化购物车存储
    if (!localStorage.getItem('cartItems')) {
        localStorage.setItem('cartItems', JSON.stringify([]));
    }

    // 加入购物车按钮事件
    document.querySelectorAll('.cart').forEach(button => {
        button.addEventListener('click', (e) => {
            const product = e.target.closest('.product');
            const item = {
                id: product.querySelector('img').src.split('/').pop(), // 使用图片名作为ID
                name: product.querySelector('.name').textContent,
                price: parseFloat(product.querySelector('.price').textContent.replace('¥', '')),
                quantity: 1,
                image: product.querySelector('img').src
            };

            const cartItems = JSON.parse(localStorage.getItem('cartItems'));
            const existingItem = cartItems.find(i => i.id === item.id);
            
            if (existingItem) {
                existingItem.quantity++;
            } else {
                cartItems.push(item);
            }
            
            localStorage.setItem('cartItems', JSON.stringify(cartItems));
            updateCartCounter();
        });
    });

    // 更新购物车数量显示
    function updateCartCounter() {
        const cartItems = JSON.parse(localStorage.getItem('cartItems'));
        document.querySelector('.cart_button .num').textContent = cartItems.reduce((sum, item) => sum + item.quantity, 0);
    }
    updateCartCounter();
});