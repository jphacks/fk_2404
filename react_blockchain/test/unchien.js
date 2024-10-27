const unchien = artifacts.require("Unchien");

/*
 * uncomment accounts to access the test accounts made available by the
 * Ethereum client
 * See docs: https://www.trufflesuite.com/docs/truffle/testing/writing-tests-in-javascript
 */
contract("Unchien", function (/* accounts */) {
  it("should assert true", async function () {
    await unchien.deployed();
    return assert.isTrue(true);
  });
});
