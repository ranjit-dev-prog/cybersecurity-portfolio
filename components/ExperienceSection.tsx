export default function ExperienceSection() {
  return (
    <section id="experience" className="py-20">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-black font-montserrat text-primary mb-6">Professional Experience</h2>
          <p className="text-xl text-muted-foreground">
            Proven track record in cybersecurity operations and client engagement
          </p>
        </div>

        <div className="glass rounded-3xl p-8 relative">
          <div className="absolute left-0 top-0 bottom-0 w-1 bg-gradient-to-b from-primary to-accent rounded-l-3xl"></div>

          <div className="ml-8">
            <h3 className="text-2xl font-bold font-montserrat text-foreground mb-2">Cybersecurity Specialist</h3>
            <div className="text-xl text-accent font-semibold mb-4">Nexcore Alliance</div>
            <div className="inline-block glass px-4 py-2 rounded-full text-sm font-medium text-muted-foreground mb-6">
              July 2025 - Present
            </div>

            <ul className="space-y-4">
              {[
                "Developed automated security tools reducing manual assessment time by 75%",
                "Conducted comprehensive security assessments for enterprise clients",
                "Implemented threat detection systems with improved accuracy",
                "Created detailed security reports with actionable recommendations",
                "Maintained 100% client satisfaction through effective communication and results",
              ].map((achievement, index) => (
                <li key={index} className="flex items-start text-foreground">
                  <span className="text-accent mr-3 mt-1">⚡</span>
                  <span className="leading-relaxed">{achievement}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  )
}
