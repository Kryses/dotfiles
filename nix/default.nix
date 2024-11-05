{ nixpkgs ? import <nixpkgs> { }}:
let 
  pkgs = [
    nixpkgs.home-manger
  ];
in
  nixpkgs.stdenv.mkDerivation {
    name = "env";
    buildInputs = pkgs;
  }
