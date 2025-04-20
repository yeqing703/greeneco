document.addEventListener('DOMContentLoaded', () => {
    let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    const cartContainer = document.getElementById('cart-items');
    const totalElement = document.getElementById('total');

    function updateCartCountText() {
        const totalCount = cartItems.reduce((sum, item) => sum + item.quantity, 0);
        const cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            cartCountElement.textContent = `${totalCount}件商品`;
        }
    }

    function renderCart() {
        cartContainer.innerHTML = '';

        if (cartItems.length === 0) {
            cartContainer.innerHTML = '<p>购物车为空</p>';
            totalElement.textContent = '¥0.00';
            updateCartCountText(); // 不要忘了这里也更新数量
            return;
        }

        cartItems.forEach((item, index) => {
            const div = document.createElement('div');
            div.className = 'cart-item';
            div.innerHTML = `
                <img src="${item.image}" alt="${item.name}">
                <div>
                    <h3>${item.name}</h3>
                    <p>¥${item.price.toFixed(2)}</p>
                    <div class="quantity-control">
                        <button class="decrement">-</button>
                        <span>${item.quantity}</span>
                        <button class="increment">+</button>
                    </div>
                    <div class="remove">删除</div>
                </div>
            `;
            cartContainer.appendChild(div);
        });

        updateTotal();
        updateCartCountText();
    }

    function updateTotal() {
        const total = cartItems.reduce((sum, item) => sum + item.price * item.quantity, 0);
        const totalElement = document.getElementById('total');
        const subtotalElement = document.getElementById('subtotal');
        const discountElement = document.getElementById('discount');
        const yunfElement = document.getElementById('yunf');

        // 基础总价
        totalElement.textContent = `¥${total.toFixed(2)}`;

        // 提取运费
        const shippingFee = 10.00;

        // 随机生成 1~10 之间的整数作为折扣
        const discount = Math.floor(Math.random() * 10) + 1;

        // 更新页面上的折扣显示
        if (discountElement) {
            discountElement.textContent = `¥${discount.toFixed(2)}`;
        }


        // 计算总计 subtotal
        const subtotal = total + shippingFee - discount;

        if (subtotalElement) {
            subtotalElement.textContent = `¥${subtotal.toFixed(2)}`;
        }
    }

    cartContainer.addEventListener('click', (e) => {
        const itemEl = e.target.closest('.cart-item');
        const index = [...cartContainer.children].indexOf(itemEl);

        if (e.target.classList.contains('increment')) {
            cartItems[index].quantity++;
        } else if (e.target.classList.contains('decrement')) {
            if (cartItems[index].quantity > 1) {
                cartItems[index].quantity--;
            }
        } else if (e.target.classList.contains('remove')) {
            cartItems.splice(index, 1);
        }

        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        renderCart();
    });

    document.getElementById('checkout').addEventListener('click', () => {
        const total = cartItems.reduce((sum, item) => sum + item.price * item.quantity, 0);
        const shippingFee = 10;
        const discount = Math.floor(Math.random() * 10) + 1;
        const subtotal = total + shippingFee - discount;

        // 跳转到支付页面，携带金额
        window.location.href = `pay.html?amount=${subtotal.toFixed(2)}`;
    });


    renderCart();
});
