from services.tracker import StudyTracker

def main():
    tracker = StudyTracker()
    
    # Load the existing data
    try:
        tracker.load_data()
        print("Data successfuly loaded.")
    except Exception as e:
        print(f"Impossible to load data : {e}")

    while True:
        print("\n******************************* MY STUDY TRACKER *******************************")
        print("1- Add a subject")
        print("2- Add a study session")
        print("3- Display all the subjects")
        print("4- Display the statistics of a subject")
        print("5- Need a motivation citation?")
        print("6- Save and exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name of subject: ").strip()
            try:
                tracker.add_subject(name)
                print(f"Subject '{name}' added !")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            name = input("Name of subject: ").strip()
            subj_obj = next((s for s in tracker.subjects if s.name == name), None)
            if subj_obj is None:
                print(f"The subject '{name}' does not exist.")
                continue
            try:
                tracker.add_session(name)
                print("Welldone, session added !")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            if not tracker.subjects:
                print("No subject saved.")
            for subj in tracker.subjects:
                print(f"- {subj.name}, Total study time: {subj.total_study_time()} minutes")

        elif choice == "4":
            name = input("Name of subject: ").strip()
            subj_obj = next((s for s in tracker.subjects if s.name == name), None)
            if subj_obj is None:
                print(f"The subject '{name}' does not exist.")
                continue
            print(f"Statistics for '{subj_obj.name}':")
            print(f"Total study time: {subj_obj.total_study_time()} minutes")
            if subj_obj.sessions:
                print("Detailed sessions:")
                for s in subj_obj.sessions:
                    print(f"  - Date: {s.date.date()}, Duration: {s.duration} min, Notes: {s.notes}")

        elif choice == "5":
            try:
                quote = tracker.get_motivation()
                print(f"Citation: {quote}")
            except Exception as e:
                print(f"Impossible to retrieve the citation : {e}")

        elif choice == "6":
            try:
                tracker.save_data()
                print("Data saved. See you next time !")
            except Exception as e:
                print(f"Error while trying to save : {e}")
            break

        else:
            print("Invalide option. Choose a number in between 1 and 6.")

if __name__ == "__main__":
    main()