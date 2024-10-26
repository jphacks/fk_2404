const myNFT = artifacts.require("unchien");


module.exports = function(_deployer) {
  // Use deployer to state migration tasks.
  _deployer.deploy(myNFT);
};

