const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type} alert-dismissible" role="alert">
            ${msg}
        </div>
    `
}