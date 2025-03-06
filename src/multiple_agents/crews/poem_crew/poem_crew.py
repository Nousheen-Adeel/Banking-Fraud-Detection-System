from crewai import Crew, Task, Agent

class PoemCrew:
    def crew(self) -> Crew:
        writer = Agent(
            name="Writer",
            role="Creative Writer",
            goal="Write beautiful poems",
            backstory="An experienced poet with a creative mind"
        )

        write_task = Task(
            description="Write a poem with {sentence_count} sentences",
            agent=writer
        )

        return Crew(
            agents=[writer],
            tasks=[write_task]
        ) 