<script>
  import Slider from "components/Slider";
  let value = 5;

</script>



<div class="container max-w-xl items-center flex flex-col">
  
  <h4 class="my-8">Coin Flip Simulator</h4>
  <caption>Number of coin flips: {value}</caption>
  <Slider min="1" max="100" bind:value />
</div>
