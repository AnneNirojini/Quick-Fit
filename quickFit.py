# Quick Fit Memory Allocation Console Program

class QuickFit:
    def __init__(self):
        # Initialize size-specific memory block lists
        self.memory_blocks = {
            "30 KB": ["Block 1", "Block 2"],
            "60 KB": ["Block 3", "Block 4"],
            "120 KB": ["Block 5", "Block 6"]
        }
        self.small_block_list = []  # List to store remaining smaller blocks

    def allocate_memory(self, process_name, required_size):
        print(f"\nAllocating memory for {process_name} ({required_size})...")
        
        # Check for exact match
        if required_size in self.memory_blocks:
            if self.memory_blocks[required_size]:
                block = self.memory_blocks[required_size].pop(0)
                print(f"{process_name} allocated {block} from {required_size} list.")
                return
            else:
                print(f"No blocks available in {required_size} list.")
        
        # Use best-fit strategy
        for size, blocks in self.memory_blocks.items():
            size_value = int(size.split()[0])  # Extract numeric size
            if size_value > int(required_size.split()[0]) and blocks:
                block = blocks.pop(0)
                print(f"{process_name} allocated {block} from {size} list.")
                
                # Calculate remaining size after split
                remaining_size = size_value - int(required_size.split()[0])
                if remaining_size > 0:
                    self.small_block_list.append(f"{remaining_size} KB Block")
                    print(f"Remaining {remaining_size} KB block added to small block list.")
                return
        
        print(f"Unable to allocate memory for {process_name}.")

    def display_memory_state(self):
        print("\nCurrent Memory State:")
        for size, blocks in self.memory_blocks.items():
            print(f"{size} List: {blocks}")
        print(f"Small Block List: {self.small_block_list}")


# Initialize memory and processes
memory_manager = QuickFit()
processes = [
    ("Process X", "30 KB"),
    ("Process Y", "60 KB"),
    ("Process Z", "100 KB"),
    ("Process W", "50 KB")
]

# Allocate memory for each process
for process_name, size in processes:
    memory_manager.allocate_memory(process_name, size)
    memory_manager.display_memory_state()
