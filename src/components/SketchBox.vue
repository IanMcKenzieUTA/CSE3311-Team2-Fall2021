<template>
  <div id = "canvasContainer">
      <canvas id="canvas"/>
  </div>
</template>

<script>
export default {
  name: 'SketchBox',
}
</script>

<style scoped>
    #canvas{
        width: 95%;
        height: 600px;
        color: gray;
        border: 1px solid black;
        
    }
</style>