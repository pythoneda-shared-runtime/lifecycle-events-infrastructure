# Infrastructure support for (runtime) lifecycle events

This package declares the infrastructure support for events relevant to the runtime lifecycle of domains.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-runtime/lifecycle-events-infrastructure/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-runtime-lifecycle-events-infrastructure = {
      [optional follows]
      url =
        "github:pythoneda-shared-runtime-def/lifecycle-events-infrastructure/[version]";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is managed by the [https://github.com/pythoneda-shared-runtime-def/lifecycle-events-infrastructure](lifecycle-events-infrastructure "lifecycle-events-infrastructure") definition repository.

