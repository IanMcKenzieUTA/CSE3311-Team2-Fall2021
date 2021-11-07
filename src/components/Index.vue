<template>
  <div id="global">
    <div id="header">
      <p>Small header here with app name</p>
    </div>
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
        <div id="containerSmall">
          <canvas id="canvas"/>
          <div id="rightButtons">
            <div id="iconChoice">
              <input type="radio" id="PredictionRBTN0" name="grp1" value="option 0">
              <p>option 0</p>
              <input type="radio" id="PredictionRBTN0" name="grp1" value="option 1">
              <p>option 1</p>
              <input type="radio" id="PredictionRBTN0" name="grp1" value="option 2">
              <p>option 2</p>
              <b-button variant="success" >complete icon</b-button>
            </div>
            <b-button @click="tabIndex=2" variant="success" id="submitButton">
              <b-icon icon="check-circle" aria-hidden="true"/>
            </b-button>
          </div>
        </div>
      </div>
      <div id = "otherInfo">
        <b-card no-body id="tabs">
          <b-tabs card v-model="tabIndex">
            <b-tab title="Tutorial" active>
              <Tutorial/>
            </b-tab>
            <b-tab title="Cheat sheet">
              <img alt="Vue logo" src="../assets/cheatSheet.png">
            </b-tab>
            <b-tab title="Results">
              <div id="container">
                <b-button variant="success" id="navButton">
                  <b-icon icon="hand-thumbs-up" aria-hidden="true"/>
                </b-button>
                <b-button variant="danger" id="navButton">
                  <b-icon icon="hand-thumbs-down" aria-hidden="true"/>
                </b-button>
              </div>
              <p>Result contents</p>
            </b-tab>
          </b-tabs>
        </b-card>
      </div>
    </div>
    <div id="footer">
      <p>Small footer here with feedback link</p>
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
#global{
  padding-top:0px;
  padding-bottom:20px;
}
#header{
  width: 100%;
  padding: 10px;
  background-color: #116466;
  color: #FFFFFF;
  border-bottom: 2px solid #000000;
}
#container > div
{
    display: inline-block;
    width: 45%;
    height: 100%;
    vertical-align: top;
    padding-top: 10px;
}
#container
{
    vertical-align: top;
    text-align: center;
    margin: 0px auto;
    width: 100%;
    height: 100%;
}   
#containerSmall > div
{
    display: inline-block;
    padding-top: 10px;
}
#iconChoice{
  margin-bottom: 300px;
}
#containerSmall
{
    text-align: center;
    margin: 0px;
    width: 100%;
    height: 100%;
}  
#submitButton
{
  vertical-align: bottom;
   text-align: left;
}
#tabs{
  background:#FFCB9A;
}

#canvas{
  width: 45%;
  height: 600px;
  background: rgb(235, 234, 234);
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
  margin-right: 70px;
}
#footer{
  position: fixed;
  width: 100%;
  padding: 10px;
  padding-top: 5px;
  bottom: 0px;
  background-color: #116466;
  color: #FFFFFF;
  border-top: 2px solid #000000;
}
</style>
