<script lang="ts">
import MenuItem from "$lib/components/UI/MenuItem.svelte";
import { createEventDispatcher } from 'svelte';

export let title = '';
export let category_id = '';
export let products:any;

let show = false;

const dispatch = createEventDispatcher();
    

function toggle_menu() {
    show = ! show
}
console.log(products)
</script>
<div id="Burgers" class="menu-category" on:click={toggle_menu}>
    <div class="menu-category-title collapse-toggle" role="tab" data-target="#{category_id}" data-toggle="collapse" aria-expanded="{show ? 'true' : 'false'}">
        <div class="bg-image" style='background-image: url("http://localhost:5173/img/Bunny_chow.jpg");'><img src="http://localhost:5173/img/kota.jpg" alt=""></div>
        <h2 class="title">{title}</h2>
    </div>
    <div id="{category_id}" class="menu-category-content collapse {show ? 'show' : ''}">
        {#each products as product}
        <MenuItem name={product.name} price={product.price} product_ingredients={product.product_ingredients}/>
        {/each}
        
    </div>
</div>