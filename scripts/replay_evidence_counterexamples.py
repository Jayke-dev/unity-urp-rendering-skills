#!/usr/bin/env python3
"""Synthetic counterexamples: this is not a Unity Frame Debugger implementation."""
import json


def colour_transition_vs_writer(initial_colour, writes):
    """All inputs represent writes to ONE synthetic opaque pixel, not GPU samples."""
    colour = initial_colour
    last_transition = last_writer = None
    for event, new_colour in writes:
        last_writer = event
        if new_colour != colour:
            last_transition = event
        colour = new_colour
    return {"last_colour_transition": last_transition, "last_writer": last_writer}


def anchors_changed(before, after, anchors):
    """Whole-image inequality is not positive evidence at a required control cohort."""
    if len(before) != len(after) or not anchors:
        raise ValueError("same-sized images and a nonempty anchor cohort required")
    if any(type(i) is not int or not 0 <= i < len(before) for i in anchors):
        raise ValueError("anchor outside image")
    return sum(before[i] != after[i] for i in anchors)


class PartialEnable:
    def __init__(self):
        self.enabled = False

    def enable_then_raise(self):
        self.enabled = True
        raise RuntimeError("synthetic setter failed after its side effect")


def enable_attempt_with_cleanup(state):
    """Small synchronous ownership model only; Unity/nested iterators need own tests."""
    if state.enabled:
        raise ValueError("not owned: already enabled")
    attempted = False
    try:
        attempted = True
        state.enable_then_raise()
    finally:
        if attempted:
            state.enabled = False


def main():
    state = PartialEnable()
    try:
        enable_attempt_with_cleanup(state)
    except RuntimeError:
        pass  # Expected synthetic failure; cleanup result is reported, not a native pass.
    print(json.dumps({
        "synthetic": True,
        "same_colour_write": colour_transition_vs_writer("black", [("draw-a", "red"), ("draw-b", "red")]),
        "irrelevant_endpoint_change": {"whole_image_changed": True,
                                       "anchor_transitions": anchors_changed(["red", "black"], ["red", "white"], [0])},
        "partial_enable_failure": {"enabled_after_cleanup": state.enabled},
        "limit": "Logical examples only; no Unity event, target, GPU sample or native capability proof.",
    }, indent=2))


if __name__ == "__main__":
    main()
