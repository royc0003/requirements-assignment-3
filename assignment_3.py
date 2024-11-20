from goalmodeling.schema import *

# Agents and Operations for Countermeasures
encryption_agent = Agent(name="Encryption Agent", agent_type=AgentType.SOFTWARE_AGENT)
multi_factor_auth_operation = Operation(name="Implement Multi-Factor Authentication", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)
scalable_infrastructure_agent = Agent(name="Infrastructure Scaling Agent", agent_type=AgentType.SOFTWARE_AGENT)
load_balancing_operation = Operation(name="Implement Load Balancing and Auto-Scaling", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)
ai_filter_agent = Agent(name="AI Filter Agent", agent_type=AgentType.SOFTWARE_AGENT)
ai_filter_operation = Operation(name="Context-Aware Filtering", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

# Obstacles and Resolutions
unauthorized_access = Obstacle(name="Unauthorized Access to Data")
downtime = Obstacle(name="High Traffic Downtime")
inaccurate_filtering = Obstacle(name="Inaccurate Content Filtering")

# Resolution Links
unauthorized_resolution = ResolutionLink(
    goal=AchieveGoal(
        name="Prevent Unauthorized Access",
        performs=[PerformanceLink(encryption_agent, multi_factor_auth_operation)]),
    obstacle=unauthorized_access)

downtime_resolution = ResolutionLink(
    goal=AchieveGoal(
        name="Mitigate High Traffic Downtime",
        performs=[PerformanceLink(scalable_infrastructure_agent, load_balancing_operation)]),
    obstacle=downtime)

filtering_resolution = ResolutionLink(
    goal=AchieveGoal(
        name="Improve Filtering Accuracy",
        performs=[PerformanceLink(ai_filter_agent, ai_filter_operation)]),
    obstacle=inaccurate_filtering)

# Update the goal model
output = generate_graph(
    goals=[
        unauthorized_resolution.goal,
        downtime_resolution.goal,
        filtering_resolution.goal],
    links=[unauthorized_resolution, downtime_resolution, filtering_resolution])

print(output)

# Generate Mermaid link
config = {"theme": "default", "themeVariables": {"fontFamily": "Helvetica"}}
link = generate_pako_link(output, "edit", config=config)
print("Mermaid Link:", link)
