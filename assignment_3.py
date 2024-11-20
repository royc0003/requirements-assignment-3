from goalmodeling.schema import *

# Define Agents, Actions (Operations), and Performance Links
notification_agent = Agent(name="Notification Agent", agent_type=AgentType.SOFTWARE_AGENT)
notification_action = Operation(name="Send notification to users about new interactions", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

content_agent = Agent(name="Content Agent", agent_type=AgentType.SOFTWARE_AGENT)
content_action = Operation(name="Analyze user preferences to suggest relevant content", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

filtering_agent = Agent(name="Filtering Agent", agent_type=AgentType.SOFTWARE_AGENT)
filtering_action = Operation(name="Automatically filter inappropriate content", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

manual_review_agent = Agent(name="Human Moderator", agent_type=AgentType.SOFTWARE_AGENT)
manual_review_action = Operation(name="Reviews flagged content for context and adherence to guidelines.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

user_report_and_feedback_agent = Agent(name="Community Management Agent", agent_type=AgentType.SOFTWARE_AGENT)
user_report_and_feedback_action = Operation(name="Processes user reports and feedback, escalating content for further review if necessary.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

final_approval_agent = Agent(name="Compliance Officer Agent", agent_type=AgentType.SOFTWARE_AGENT)
final_approval_action = Operation(name="Conducts a final review for legal, community, and platform guideline compliance.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

publishing_agent = Agent(name="Publishing Agent", agent_type=AgentType.SOFTWARE_AGENT)
publishing_action = Operation(name="Publishes vetted content, ensuring it meets all moderation requirements.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)


report_agent = Agent(name="Report Agent", agent_type=AgentType.SOFTWARE_AGENT)
report_action = Operation(name="Provide reporting tool for user-generated issues", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

encryption_agent = Agent(name="Encryption Agent", agent_type=AgentType.SOFTWARE_AGENT)
encryption_action = Operation(name="Encrypt sensitive user data", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

guideline_agent = Agent(name="Guideline Agent", agent_type=AgentType.SOFTWARE_AGENT)
guideline_action = Operation(name="Enforce data-sharing guidelines", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

personalization_agent = Agent(name="Personalization Agent", agent_type=AgentType.SOFTWARE_AGENT)
personalization_action = Operation(name="Customize user experience based on preferences", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

loyalty_agent = Agent(name="Loyalty Agent", agent_type=AgentType.SOFTWARE_AGENT)
loyalty_action = Operation(name="Provide rewards for long-term usage", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

authentication_agent = Agent(name="Authentication Agent", agent_type=AgentType.SOFTWARE_AGENT)
auth_action = Operation(name="Implement and manage 2-Factor Authentication", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

security_monitoring_agent = Agent(name="Security Monitoring Agent", agent_type=AgentType.SOFTWARE_AGENT)
security_action = Operation(name="Monitor login anomalies for security", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

performance_agent = Agent(name="Performance Agent", agent_type=AgentType.SOFTWARE_AGENT)
performance_action = Operation(name="Optimize server response times", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

infrastructure_agent = Agent(name="Infrastructure Agent", agent_type=AgentType.SOFTWARE_AGENT)
load_balance_action = Operation(name="Manage load balancing across servers", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

system_monitoring_agent = Agent(name="System Monitoring Agent", agent_type=AgentType.SOFTWARE_AGENT)
rapid_response_action = Operation(name="Implement rapid-response system for downtime", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)
health_monitoring_action = Operation(name="Continuously monitor service health", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

email_onboarding_agent = Agent(name="Email Onboarding Agent", agent_type=AgentType.SOFTWARE_AGENT)
email_onboarding_action = Operation(name="Sends a verification email, monitors link confirmation, and activates the account upon email verification.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

social_media_onboarding_agent = Agent(name="Social Media Onboarding Agent", agent_type=AgentType.SOFTWARE_AGENT)
social_media_onboarding_action = Operation(name="Authenticates via social media, retrieves user info, links the account, and activates the user account.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

phone_onboarding_agent = Agent(name="Phone Onboarding Agent	", agent_type=AgentType.SOFTWARE_AGENT)
phone_onboarding_action = Operation(name="Sends an OTP to the phone, verifies OTP input, and activates the account upon phone verification.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)


'''
email_registration = AchieveGoal(name="Email Registration",
                                  performs=[PerformanceLink(agent=filtering_agent, operation=filtering_action)], leaf=True)
social_media_linking = AchieveGoal(name="Social Media Account Linking",
                                  performs=[PerformanceLink(agent=filtering_agent, operation=filtering_action)], leaf=True)
phone_number_verification = AchieveGoal(name="Phone Number Verification",
                                  performs=[PerformanceLink(agent=filtering_agent, operation=filtering_action)], leaf=True)
'''


# Define Low-Level Goals with Performance Links
notify_interactions = MaintainGoal(name="Notify Users of New Interactions UNLESS Prolonged Platform Downtime",
                                  performs=[PerformanceLink(agent=notification_agent, operation=notification_action)], leaf=True)
suggest_content = MaintainGoal(name="Suggest Relevant Content UNLESS Prolonged Platform Downtime",
                              performs=[PerformanceLink(agent=content_agent, operation=content_action)], leaf=True)
automated_filtering = AchieveGoal(name="Automated Content Filtering",
                                  performs=[PerformanceLink(agent=filtering_agent, operation=filtering_action)], leaf=True)
email_registration = AchieveGoal(name="Email Registration",
                                  performs=[PerformanceLink(agent=email_onboarding_agent, operation=email_onboarding_action)], leaf=True)
social_media_linking = AchieveGoal(name="Social Media Account Linking",
                                  performs=[PerformanceLink(agent=social_media_onboarding_agent, operation=social_media_onboarding_action)], leaf=True)
phone_number_verification = AchieveGoal(name="Phone Number Verification",
                                  performs=[PerformanceLink(agent=phone_onboarding_agent, operation=phone_onboarding_action)], leaf=True)
'''
filtering_agent = Agent(name="Filtering Agent", agent_type=AgentType.SOFTWARE_AGENT)
filtering_action = Operation(name="Automatically filter inappropriate content", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

manual_review_agent = Agent(name="Human Moderator", agent_type=AgentType.SOFTWARE_AGENT)
manual_review_action = Operation(name="Reviews flagged content for context and adherence to guidelines.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

user_report_and_feedback_agent = Agent(name="Community Management Agent", agent_type=AgentType.SOFTWARE_AGENT)
user_report_and_feedback_action = Operation(name="Processes user reports and feedback, escalating content for further review if necessary.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

final_approval_agent = Agent(name="Compliance Officer Agent", agent_type=AgentType.SOFTWARE_AGENT)
final_approval_action = Operation(name="Conducts a final review for legal, community, and platform guideline compliance.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

publishing_agent = Agent(name="Publishing Agent", agent_type=AgentType.SOFTWARE_AGENT)
publishing_action = Operation(name="Publishes vetted content, ensuring it meets all moderation requirements.", category=OperationCategory.SOFTWARE_TO_BE_OPERATION)

'''
manual_review = AchieveGoal(name="Manual Review of Flagged Content",
                                  performs=[PerformanceLink(agent=manual_review_agent, operation=manual_review_action)], leaf=True)
user_report_and_feedback = AchieveGoal(name="User Reporting and Feedback Processing",
                                  performs=[PerformanceLink(agent=user_report_and_feedback_agent, operation=user_report_and_feedback_action)], leaf=True)
final_approval = AchieveGoal(name="Final Approval for Publishing",
                                  performs=[PerformanceLink(agent=final_approval_agent, operation=final_approval_action)], leaf=True)
content_moderation_complete = AchieveGoal(name="Content Moderation Completed",
                                  performs=[PerformanceLink(agent=publishing_agent, operation=publishing_action)], leaf=True)
user_reporting = AchieveGoal(name="User-Generated Issue Reporting",
                             performs=[PerformanceLink(agent=report_agent, operation=report_action)], leaf=True)
encrypt_data = AchieveGoal(name="Data Encryption",
                           performs=[PerformanceLink(agent=encryption_agent, operation=encryption_action)], leaf=True)
enforce_guidelines = AchieveGoal(name="Data-Sharing Guidelines Enforcement",
                                 performs=[PerformanceLink(agent=guideline_agent, operation=guideline_action)], leaf=True)
personalize_experience = AchieveGoal(name="Personalize User Experience",
                                     performs=[PerformanceLink(agent=personalization_agent, operation=personalization_action)], leaf=True)
reward_usage = AchieveGoal(name="Reward Long-Term Usage",
                           performs=[PerformanceLink(agent=loyalty_agent, operation=loyalty_action)], leaf=True)
two_factor_auth = AchieveGoal(name="Implement 2-Factor Authentication",
                              performs=[PerformanceLink(agent=authentication_agent, operation=auth_action)], leaf=True)
monitor_logins = AchieveGoal(name="Monitor Login Anomalies",
                             performs=[PerformanceLink(agent=security_monitoring_agent, operation=security_action)], leaf=True)
optimize_server = AchieveGoal(name="Optimize Server Response Times",
                              performs=[PerformanceLink(agent=performance_agent, operation=performance_action)], leaf=True)
load_balancing = AchieveGoal(name="Load Balancing",
                             performs=[PerformanceLink(agent=infrastructure_agent, operation=load_balance_action)], leaf=True)
rapid_response = AchieveGoal(name="Implement Rapid-Response System",
                             performs=[PerformanceLink(agent=system_monitoring_agent, operation=rapid_response_action)], leaf=True)
health_monitoring = AchieveGoal(name="Service Health Monitoring",
                                performs=[PerformanceLink(agent=system_monitoring_agent, operation=health_monitoring_action)], leaf=True)

# Define Mid-Level Goals with Refinements
user_onboarding = AchieveGoal(name="User Onboarding",
                             refinements=[Refinement(complete=False, children=[email_registration]), Refinement(complete=False, children=[social_media_linking]), Refinement(complete=False, children=[phone_number_verification])], annotation="Tactic: Decomposition-by-Case Pattern")
user_engagement = MaintainGoal(name="Condition1: Notify Users of New Interaction and Condition 2: Suggest Relevant Content UNLESS Prolonged Platform Downtime",
                              refinements=[Refinement(complete=False, children=[notify_interactions, suggest_content])], annotation="Tactic: Divide-and-Conquer Pattern")
content_moderation = AchieveGoal(name="Content Moderation",
                                 refinements=[Refinement(complete=True, children=[automated_filtering, user_reporting, manual_review, user_report_and_feedback, final_approval, content_moderation_complete])], annotation = "Tactic: Milestone-Driven Pattern")
user_retention = AchieveGoal(name="User Retention",
                             refinements=[Refinement(complete=False, children=[personalize_experience, reward_usage])])
data_privacy = AchieveGoal(name="Data Privacy Compliance",
                           refinements=[Refinement(complete=False, children=[encrypt_data, enforce_guidelines])])
auth_integrity = MaintainGoal(name="User Authentication Integrity",
                              refinements=[Refinement(complete=True, children=[two_factor_auth, monitor_logins])], annotation="Tactic: Guard Introduction Pattern")
platform_performance = MaintainGoal(name="Consistent Platform Performance",
                                    refinements=[Refinement(complete=False, children=[optimize_server, load_balancing])])
avoid_downtime = AvoidGoal(name="Avoid Prolonged Downtime",
                           refinements=[Refinement(complete=False, children=[rapid_response, health_monitoring])], annotation="Tactic: Unmonitorability and Uncontrollability Patterns")

# Define High-Level Goals with Refinements
user_satisfaction = AchieveGoal(name="User Satisfaction",
                                refinements=[Refinement(complete=False, children=[user_engagement, content_moderation, user_retention, user_onboarding])])
platform_security = AchieveGoal(name="Platform Security",
                                refinements=[Refinement(complete=False, children=[data_privacy, auth_integrity])])
system_reliability = MaintainGoal(name="System Reliability",
                                  refinements=[Refinement(complete=False, children=[platform_performance, avoid_downtime])])

# Define obstacle

#  Impediment towards Achieve [Platform Security]
unauthorized_access_to_user_data = Obstacle(
    name="Unauthorized access to user data"
)

# Impediment towards Maintain [System Reliability]
server_crashes_under_high_traffic = Obstacle(
    name="Server crashes under high traffic"
)

# Impediment towards Achieve [Content Moderation]
incomplete_automated_content_filterin = Obstacle(
    name="Incomplete automated content filtering"
)

# Obstacle 2 Sub-Obstacles
insufficient_capacity = Obstacle(
    name="Insufficient server capacity to handle peak traffic"
)
inefficient_load_balancing = Obstacle(
    name="Inefficient load balancing during high traffic"
)
server_crashes_and_refinement = Refinement(
    complete=False,  # AND-refinement
    children=[insufficient_capacity, inefficient_load_balancing]
)


# Resolutions for Obstacle 2 Sub-Obstacles
auto_scaling_goal = AchieveGoal(
    name="Implement Auto-Scaling Infrastructure",
    leaf=True
)
load_balancing_goal = AchieveGoal(
    name="Optimize Load Balancing Mechanisms",
    leaf=True
)

# Resolution Links for Obstacle 2
auto_scaling_resolution_link = ResolutionLink(goal=auto_scaling_goal, obstacle=insufficient_capacity)
load_balancing_resolution_link = ResolutionLink(goal=load_balancing_goal, obstacle=inefficient_load_balancing)

# Integrating Obstacles and Refinements into Goal Model
server_crashes_obstacle = Obstacle(
    name="Server crashes under high traffic",
    refinements=[server_crashes_and_refinement],
    annotation="Obstruction Link to Goal: Maintain[System Reliability]"
)


# Obstruct Links
platform_unauthorized_ob_link = ObstructionLink(
    goal=platform_security,
    obstacle=unauthorized_access_to_user_data
)

server_crash_ob_link = ObstructionLink(
    goal=system_reliability,
    obstacle=server_crashes_obstacle
)




mfa_resolution = AchieveGoal(
    name="1.1 Implement Multi-Factor Authentication (Enhance Authentication Mechanism)",
    leaf=True
)

encryption_audit_resolution = AchieveGoal(
    name="1.2 Data Encryption at Rest and In Transit (AES-256)",
    leaf=True
)

# Define Obstruction Links

# Define Resolution Link
resolution_enhance_unauth_link = ResolutionLink(
    goal=mfa_resolution,
    obstacle=unauthorized_access_to_user_data  
)

resolution_data_encryption_unauth_link = ResolutionLink(
    goal=encryption_audit_resolution,
    obstacle=unauthorized_access_to_user_data
)

# resolution_mfa = ResolutionLink(goal=mfa_resolution, obstacle=unauthorized_access_obstacle)
# resolution_encryption_audit = ResolutionLink(goal=encryption_audit_resolution, obstacle=no_encryption_audit_obstacle)
# resolution_auto_scaling = ResolutionLink(goal=auto_scaling_resolution, obstacle=server_crash_obstacle)
# resolution_load_testing = ResolutionLink(goal=load_testing_resolution, obstacle=server_crash_obstacle)
# resolution_ai_filtering = ResolutionLink(goal=ai_filtering_resolution, obstacle=incomplete_filtering_obstacle)
# resolution_hybrid_moderation = ResolutionLink(goal=hybrid_moderation_resolution, obstacle=incomplete_filtering_obstacle)

# # Integrate Obstacles into the Goal Model using Refinements
# auth_integrity = MaintainGoal(
#     name="User Authentication Integrity",
#     refinements=[Refinement(complete=False, children=[unauthorized_access_obstacle])],
#     annotation="Tactic: Guard Introduction Pattern"
# )
# data_privacy = AchieveGoal(
#     name="Data Privacy Compliance",
#     refinements=[Refinement(complete=False, children=[no_encryption_audit_obstacle])],
#     annotation="Tactic: Security Compliance"
# )
# platform_performance = MaintainGoal(
#     name="Consistent Platform Performance",
#     refinements=[Refinement(complete=False, children=[server_crash_obstacle])],
#     annotation="Tactic: System Performance Optimization"
# )
# content_moderation = AchieveGoal(
#     name="Content Moderation",
#     refinements=[Refinement(complete=False, children=[incomplete_filtering_obstacle])],
#     annotation="Tactic: Milestone-Driven Pattern"
# )

# Obstacle 3 Sub-Obstacles
inaccurate_detection = Obstacle(
    name="Inaccurate detection of inappropriate content"
)
limited_handling_edge_cases = Obstacle(
    name="Limited handling of edge cases in automated filtering"
)
content_filtering_or_refinement = Refinement(
    complete=False,  # OR-refinement
    children=[inaccurate_detection, limited_handling_edge_cases]
)

incomplete_automated_filtering_obstacle = Obstacle(
    name="Incomplete automated content filtering ",
    refinements=[content_filtering_or_refinement],
    annotation="Obstruction Link to Goal: Content Moderation"
)

# Resolutions for Obstacle 3 Sub-Obstacles
ai_filtering_goal = AchieveGoal(
    name="Leverage AI for Context-Aware Moderation",
    leaf=True
)
hybrid_moderation_goal = AchieveGoal(
    name="Implement Hybrid Moderation System",
    leaf=True
)

# Resolution Links for Obstacle 3
ai_filtering_resolution_link = ResolutionLink(goal=ai_filtering_goal, obstacle=inaccurate_detection)
hybrid_moderation_resolution_link = ResolutionLink(goal=hybrid_moderation_goal, obstacle=limited_handling_edge_cases)

incomplete_automated_content_filterin_link = ObstructionLink(
    goal=content_moderation,
    obstacle=incomplete_automated_filtering_obstacle
)


output = generate_graph(goals=[user_satisfaction, platform_security, system_reliability], links=[platform_unauthorized_ob_link,resolution_enhance_unauth_link, resolution_data_encryption_unauth_link, auto_scaling_resolution_link, load_balancing_resolution_link, server_crash_ob_link, ai_filtering_resolution_link, hybrid_moderation_resolution_link, incomplete_automated_content_filterin_link])

print(output)

config = {"theme": "default", "themeVariables": {"fontFamily": "Helvetica"}}
link = generate_pako_link(output, "edit", config=config)
print("Mermaid Link:", link)
