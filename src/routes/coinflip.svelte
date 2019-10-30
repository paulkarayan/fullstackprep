<script>
  import Slider from "components/Slider";
  let value = 5;

  let rand = -1;
  function getRand() {
    fetch("http://localhost:5000/rand")
      .then(response => {
        return response.json()
      })
      .then(data => {
        // Work with JSON data here
        console.log(data['data'])
        rand = data['data']
      })
      .catch(err => {
        // Do something for an error here
    })
  }

</script>

<h1>Your number is {rand}!</h1>
<button on:click={getRand}>Get a random number</button>

<div class="container max-w-xl items-center flex flex-col">
  
  <h4 class="my-8">Coin Flip Simulator</h4>
  <caption>Number of coin flips: {value}</caption>
  <Slider min="1" max="100" bind:value />
</div>
