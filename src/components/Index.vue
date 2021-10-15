<template>
  <div>
    <div id="container">
      <div id = "sketchbox">
        <div id="container">
          <b-button variant="secondary" id="navButton">
            <b-icon icon="arrow90deg-left" aria-hidden="true"/>
          </b-button>
          <b-button variant="secondary" id="navButton">
            <b-icon icon="arrow90deg-right" aria-hidden="true"/>
          </b-button>
          <b-button variant="warning" id="refreshCan">
            <b-icon icon="arrow-counterclockwise" aria-hidden="true"/>
          </b-button>
        </div>
        <div id="container">
          <canvas id="canvas"/>
            <b-button @click="tabIndex=2" variant="success" id="submitButton">
              <b-icon icon="check-circle" aria-hidden="true"/>
            </b-button>
        </div>
      </div>
      <div id = "otherInfo">
        <b-card no-body>
          <b-tabs card v-model="tabIndex">
            <b-tab title="Tutorial" active>
              <Tutorial/>
            </b-tab>
            <b-tab title="Cheat sheet">
              <img alt="Vue logo" src="../assets/cheatSheet.png">
            </b-tab>
            <b-tab title="Results">
              <p>Result contents</p>
            </b-tab>
          </b-tabs>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>

import Tutorial from './Tutorial.vue'
export default {
  name: 'Index',
  components:{
    Tutorial
  },
  data() {
      return {
        tabIndex: 1
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#container > div
{
    display: inline-block;
    width: 45%;
    height: 100%;
    vertical-align: top;
}
#container
{
    vertical-align: top;
    text-align: center;
    margin: 0px auto;
    width: 100%;
    height: 100%;
}   
#submitButton
{
  vertical-align: bottom;
}
#canvas{
  width: 45%;
  height: 600px;
  color: gray;
  border: 1px solid black;
  margin-right: 10px;
  margin-top: 5px;
}
#navButton{
  position: relative;
  margin: 5px;
}
#refreshCan{
  margin-left: 160px;
}
</style>
