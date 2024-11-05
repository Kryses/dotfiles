{
  description = "Kryses Home";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = inputs@{ self, nixpkgs, home-manager }:
    let
      configuration = { pkgs, ... }: {
        enviromnet.systemPackages = with pkgs;
          [
            vim
            direnv
            sshs
          ];
      };
    in
    { };
}
