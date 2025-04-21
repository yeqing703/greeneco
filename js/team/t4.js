document.getElementById("fromMessage").addEventListener("submit", function (event) {
    event.preventDefault();  // 阻止默认提交行为

    let ename = document.getElementById("ename").value.trim();
    let message = document.getElementById("message").value.trim();

    if (!ename || !message) {
        alert("请填写完整信息！");
        return;
    }

    console.log("ename:", ename);
    console.log("message:", message);

    fetch("/contact", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ename: ename, message: message })
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                // 显示弹窗和遮罩
                document.getElementById("popup").style.display = "block"
                document.getElementById("popup-mask").style.display = "block"

                // 清空表单
                document.getElementById("fromMessage").reset()

                // 2秒后自动隐藏
                setTimeout(() => {
                    document.getElementById("popup").style.display = "none"
                    document.getElementById("popup-mask").style.display = "none"
                }, 2000)
            } else {
                alert("提交失败: " + data.message)
            }
        })
});






