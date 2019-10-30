<script>
  import Slider from "components/Slider";
  $: value = 5;
  
  let heads = 0 
  let tails = 0 

  function getFlip(value) {
    console.log(value, "<----")
    fetch("http://localhost:5000/coinflips/34")
      .then(response => {
        return response.json()
      })
      .then(data => {
        // Work with JSON data here
        console.log(data['heads'], data['tails'])
        $: heads = data['heads']
        $: tails = data['tails']
      })
      .catch(err => {
        // Do something for an error here
    })
  }

</script>


<div class="container max-w-xl items-center flex flex-col">
  Heads {heads}
  Tails {tails}
  <h4 class="my-8">Coin Flip Simulator</h4>
  <caption>Number of coin flips: {value}</caption>
  <Slider min="1" max="100" bind:value on:change = {getFlip} />

</div>
