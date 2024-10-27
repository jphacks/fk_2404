// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ToiletProofNFT is ERC721, Ownable {
    using EnumerableSet for EnumerableSet.UintSet;
    EnumerableSet.UintSet private _tokenIds;

    struct ProofData {
        uint256 startTime; 
        uint256 endTime;
        string label;
        string macAddr;
        string score;
    }

    mapping(uint256 => ProofData) private _proofData;

    constructor() ERC721("ToiletProofNFT", "TPNFT") {}

    function mintNFT(
        address recipient,
        uint256 startTime,
        uint256 endTime,
        string memory label,
        string memory macAddr,
        string memory score
    ) public onlyOwner returns (uint256) {
        uint256 newItemId = _tokenIds.length();
        _tokenIds.add(newItemId);
        _mint(recipient, newItemId);

        _proofData[newItemId] = ProofData({
            startTime: startTime,
            endTime: endTime,
            label: label,
            macAddr: macAddr,
            score: score
        });

        return newItemId;
    }

    function getProofData(uint256 tokenId) public view returns (ProofData memory) {
        require(_exists(tokenId), "Token does not exist");
        return _proofData[tokenId];
    }

    // Additional functions for PDF generation and QR code can be implemented here
}
