<script>
    import MenuItem from "$lib/components/UI/MenuItem.svelte";
    import { createEventDispatcher } from 'svelte';

// export let modalTitle: string = '';
// export let showCloseButton: boolean = true;
    let show = false;

const dispatch = createEventDispatcher();
    export let title = '';
    export let category_id = '';
    export let products = '';

function toggle_menu() {
    show = ! show
}

</script>
<div id="Burgers" class="menu-category" on:click={toggle_menu}>
    <div class="menu-category-title collapse-toggle" role="tab" data-target="#{category_id}" data-toggle="collapse" aria-expanded="{show ? 'true' : 'false'}">
        <div class="bg-image"><img src="http://assets.suelo.pl/soup/img/photos/menu-title-burgers.jpg" alt=""></div>
        <h2 class="title">{title}</h2>
    </div>
    <div id="{category_id}" class="menu-category-content collapse {show ? 'show' : ''}">
        <MenuItem on:viewProduct={() => {
            dispatch('viewProduct');
        }}></MenuItem>
        <MenuItem></MenuItem>
        
        
    </div>
</div>