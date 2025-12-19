// Main JS File

document.addEventListener('DOMContentLoaded', function () {
    console.log('Tourist System Loaded');

    // Add simple fade-in effect to panels
    const elements = document.querySelectorAll('.glass-panel');
    elements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.1}s`;
    });
});
