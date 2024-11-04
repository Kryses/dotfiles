{ nixpkgs ? import <nixpkgs> { }}:
let 
  pkgs = [
    nixpkgs.neovim
    nixpkgs.ripgrep
  ];
in
  nixpkgs.stdenv.mkDerivation {
    name = "env";
    buildInputs = pkgs;
  }
