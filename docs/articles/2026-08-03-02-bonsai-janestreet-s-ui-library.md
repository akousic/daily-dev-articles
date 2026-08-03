# Bonsai: Janestreet's UI Library

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 200
- **Published (UTC):** 2026-08-03 08:29
- **Original:** https://github.com/janestreet/bonsai

## Summary

Bonsai is a UI library for building performant, reactive web applications in OCaml, partly inspired by Elm. It is used to build almost all web applications inside Jane Street, everything from the corporate directory to tools that monitor and interact with our trading systems. A simple Bonsai component with a little interactivity looks like this: module Dice = struct let faces = [ "⚀"; "⚁"; "⚂"; "⚃"; "⚄"; "⚅" ] ;; let component (graph @ local) = (* Components are implemented as purely functional state machines.

## Key Takeaways

- *) let face, set_face = Bonsai.state (List.hd_exn faces) graph in (* Components are incrementally rendered, only when the relevant parts of the state change.
- *) let%arr face and set_face in {%html| <div> You rolled a #{face} <button style="" on_click=%{fun _ -> let index = Random.int (List.length faces) in set_face (List.nth_exn faces index)} > Roll the dice </button> </div> |} ;; end Components are implemented as purely functional state machines, and are easily composable.
- Incrementalization inside the framework means that values don’t get recomputed until necessary.

---
_Auto-generated daily digest entry._
