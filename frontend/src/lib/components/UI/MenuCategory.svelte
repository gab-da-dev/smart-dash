<script>
    import MenuItem from "$lib/components/UI/MenuItem.svelte";

    export let title = '';
    export let category_id = '';
    export let products = '';
</script>
<div id="Burgers" class="menu-category">
    <div class="menu-category-title collapse-toggle" role="tab" data-target="#{category_id}" data-toggle="collapse" aria-expanded="true">
        <div class="bg-image"><img src="http://assets.suelo.pl/soup/img/photos/menu-title-burgers.jpg" alt=""></div>
        <h2 class="title">{title}</h2>
    </div>
    <div id="{category_id}" class="menu-category-content collapse show">
        <MenuItem></MenuItem>
        <MenuItem></MenuItem>
        
        
    </div>
</div>