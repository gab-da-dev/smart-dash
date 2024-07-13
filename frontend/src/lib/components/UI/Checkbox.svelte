<script lang="ts">
    export let label = "rwar";
    export let value = false;
</script>

<!-- <label class="inline-flex items-center mt-3">
    <input
        bind:checked={value}
        {value}
        type="checkbox"
        class="form-checkbox h-5 w-5 text-gray-600 mr-4"
    /><span class="ml-2 text-gray-700">{label}</span>
</label> -->

<div class="flex items-start mb-6">
    <div class="flex items-center h-5">
        <input
            id="remember"
            aria-describedby="remember"
            type="checkbox"
            name="active"
            bind:checked={value}
        {value}
        
            class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded"
            
        />
    </div>
    <div class="text-sm ml-3">
        <label
            for="remember"
            class="font-medium text-gray-900 ml-4"
            >{label}</label
        >
    </div>
</div>

<!-- bind:group={value} -->