const myNFT = artifacts.require("Unchien");


module.exports = function(_deployer) {
  // Use deployer to state migration tasks.
  _deployer.deploy(myNFT);
};

