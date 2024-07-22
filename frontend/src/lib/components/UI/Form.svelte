<script>
    import { createEventDispatcher } from 'svelte';
    import validate from 'validate.js';

    // export let data = {};
    // export let constraints = {};
    export let label = '';
    let errors = {};

    const dispatch = createEventDispatcher();

    async function handleSubmit() {
        dispatch('handleSubmit');
    }
</script>

<div>
    <h2 class="text-2xl font-bold mb-4">{label}</h2>

</div>
<div>
    <slot></slot>
     <!-- <div>
            <button
                on:click={handleSubmit}
                type="button"
                class="middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg bg-gradient-to-tr from-blue-600 to-blue-400 text-white shadow-md shadow-blue-500/20 hover:shadow-lg hover:shadow-blue-500/40 active:opacity-[0.85] flex items-center gap-4 px-4 capitalize"
                >Create</button>
        </div> -->
</div>


