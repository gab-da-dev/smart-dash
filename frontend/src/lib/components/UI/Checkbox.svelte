<script lang="ts">
    export let label = "rwar";
    export let value = false;
</script>

<label class="inline-flex items-center mt-3">
    <input
        bind:checked={value}
        {value}
        bind:group={value}
        type="checkbox"
        class="form-checkbox h-5 w-5 text-gray-600 mr-4"
    /><span class="ml-2 text-gray-700">{label}</span>
</label>
