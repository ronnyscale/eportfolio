<script>
    document.querySelectorAll('#seeButton').forEach(item => {
        item.addEventListener('click', event => {
            event.preventDefault();
            window.open('detail.html', '_blank', 'height=500,width=500,top=100,left=100');
        });
    });
</script>
