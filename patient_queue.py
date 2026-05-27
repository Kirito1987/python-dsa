"""
Patient Triage Queue — Priority Queue Implementation in Python
---------------------------------------------------------------
In a hospital or telehealth setting, patients can't always be seen
in the order they arrive. A triage system prioritizes patients based
on the severity of their condition.

This module simulates that system using a Min-Heap based Priority Queue:
    - Lower severity number = higher priority (1 is critical, 5 is minor)
    - If two patients share the same severity, the one who arrived first
      is seen first (FIFO tiebreaker)

Real-world relevance:
    - MyTeleHealth(fake name used for example of program) and similar platforms route patients to providers based on
      urgency, wait time, and availability — all priority queue problems.

Data Structure: Min-Heap
    - insert (add patient):       O(log n)
    - get next patient (extract): O(log n)
    - peek at next patient:       O(1)
    - check queue:                O(1)

Python's `heapq` module implements a min-heap on a plain list.
"""

import heapq
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


# ── Severity Levels ───────────────────────────────────────────────────────────

SEVERITY_LABELS = {
    1: "Critical   🔴",
    2: "Urgent     🟠",
    3: "Moderate   🟡",
    4: "Minor      🟢",
    5: "Routine    🔵",
}


# ── Patient Data Class ────────────────────────────────────────────────────────

@dataclass
class Patient:
    """
    Represents a patient in the triage system.

    Attributes:
        name (str):          Patient's name
        severity (int):      1 (critical) to 5 (routine)
        complaint (str):     Brief description of their condition
        arrival_time (str):  Timestamp when they joined the queue
        patient_id (int):    Auto-assigned ID, used as tiebreaker
    """
    name: str
    severity: int
    complaint: str
    arrival_time: str = field(default_factory=lambda: datetime.now().strftime("%H:%M:%S"))
    patient_id: int = field(default=0)

    def __str__(self):
        label = SEVERITY_LABELS.get(self.severity, "Unknown")
        return (
            f"[ID: {self.patient_id:03d}] {self.name:<20} "
            f"| Severity: {label} "
            f"| Arrived: {self.arrival_time} "
            f"| Complaint: {self.complaint}"
        )


# ── Triage Priority Queue ─────────────────────────────────────────────────────

class TriageQueue:
    """
    A priority queue for patient triage using a Min-Heap.

    Patients are ordered by:
        1. Severity (lower number = seen first)
        2. Patient ID as tiebreaker (earlier arrival = seen first)

    The heap stores tuples: (severity, patient_id, Patient)
    This ensures Python's heapq can compare entries without needing
    to compare Patient objects directly.
    """

    def __init__(self):
        self._heap = []          # The underlying min-heap
        self._counter = 0        # Auto-incrementing patient ID
        self._total_seen = 0     # Track how many patients have been seen

    def add_patient(self, name: str, severity: int, complaint: str) -> Patient:
        """
        Register a new patient and add them to the triage queue.

        Args:
            name (str):      Patient name
            severity (int):  1–5, where 1 is most critical
            complaint (str): Description of their condition

        Returns:
            Patient: The newly created patient record
        """
        if not 1 <= severity <= 5:
            raise ValueError(f"Severity must be between 1 and 5, got {severity}")

        self._counter += 1
        patient = Patient(
            name=name,
            severity=severity,
            complaint=complaint,
            patient_id=self._counter
        )

        # Heap tuple: (severity, patient_id, patient)
        # severity first so heap sorts by urgency
        # patient_id second as a FIFO tiebreaker
        heapq.heappush(self._heap, (severity, self._counter, patient))
        return patient

    def next_patient(self) -> Optional[Patient]:
        """
        Remove and return the highest-priority patient (lowest severity number).
        Returns None if the queue is empty.

        Time Complexity: O(log n)
        """
        if self.is_empty():
            return None

        _, _, patient = heapq.heappop(self._heap)
        self._total_seen += 1
        return patient

    def peek(self) -> Optional[Patient]:
        """
        View the next patient without removing them from the queue.
        Returns None if the queue is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        _, _, patient = self._heap[0]
        return patient

    def is_empty(self) -> bool:
        """Return True if no patients are waiting."""
        return len(self._heap) == 0

    def size(self) -> int:
        """Return the number of patients currently waiting."""
        return len(self._heap)

    def display_queue(self):
        """
        Display all waiting patients in priority order.
        Note: Creates a sorted copy — does not modify the actual heap.
        """
        if self.is_empty():
            print("  No patients currently waiting.")
            return

        # Sort a copy by (severity, patient_id) to show priority order
        sorted_patients = sorted(self._heap, key=lambda x: (x[0], x[1]))
        print(f"  {'#':<5} {'Patient':<22} {'Severity':<25} {'Arrived':<12} {'Complaint'}")
        print("  " + "-" * 95)
        for rank, (_, _, patient) in enumerate(sorted_patients, 1):
            label = SEVERITY_LABELS.get(patient.severity, "Unknown")
            print(
                f"  {rank:<5} {patient.name:<22} {label:<25} "
                f"{patient.arrival_time:<12} {patient.complaint}"
            )

    def stats(self):
        """Display queue statistics."""
        print(f"  Patients waiting : {self.size()}")
        print(f"  Patients seen    : {self._total_seen}")
        print(f"  Total registered : {self._counter}")


# ── Demo: Simulated Telehealth Triage Session ─────────────────────────────────

if __name__ == "__main__":

    print("=" * 60)
    print("   MyTeleHealth TRIAGE SYSTEM — Patient Queue Demo")
    print("=" * 60)

    queue = TriageQueue()

    # ── Step 1: Patients join the queue ───────────────────────────────────────
    print("\n📋 Registering incoming patients...\n")

    patients_data = [
        ("Maria Santos",   3, "Persistent headache and mild fever"),
        ("James Okafor",   1, "Chest pain and difficulty breathing"),
        ("Linda Chen",     4, "Sore throat, no fever"),
        ("David Kim",      2, "Severe allergic reaction, hives spreading"),
        ("Sofia Reyes",    5, "Routine prescription renewal"),
        ("Amir Hassan",    3, "Abdominal pain, moderate"),
        ("Priya Patel",    1, "Unresponsive, suspected stroke"),
        ("Tom Brooks",     4, "Mild back pain, 2 days"),
    ]

    for name, severity, complaint in patients_data:
        p = queue.add_patient(name, severity, complaint)
        label = SEVERITY_LABELS[severity]
        print(f"  ✅ Registered: {p.name:<20} | {label}")

    # ── Step 2: View the full queue in priority order ─────────────────────────
    print(f"\n📊 Current Queue ({queue.size()} patients waiting):\n")
    queue.display_queue()

    # ── Step 3: See next patient without removing ─────────────────────────────
    next_up = queue.peek()
    print(f"\n👁️  Next to be seen (peek): {next_up.name} — {next_up.complaint}")

    # ── Step 4: Process patients in priority order ────────────────────────────
    print("\n🏥 Calling patients in triage order...\n")

    call_count = 0
    while not queue.is_empty():
        patient = queue.next_patient()
        call_count += 1
        label = SEVERITY_LABELS[patient.severity]
        print(f"  {call_count}. NOW SEEING: {patient.name:<20} | {label} | {patient.complaint}")

        # Simulate adding a new walk-in mid-session
        if call_count == 3:
            print("\n  🚨 Walk-in emergency!\n")
            emergency = queue.add_patient(
                "Carlos Rivera", 1, "Severe chest trauma, car accident"
            )
            print(f"  ⚡ URGENT ADD: {emergency.name} — {emergency.complaint}\n")

    # ── Step 5: Final stats ───────────────────────────────────────────────────
    print("\n📈 Session Summary:\n")
    queue.stats()
    print("\n" + "=" * 60)
    print("   All patients have been seen. Queue is empty.")
    print("=" * 60)
