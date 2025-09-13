export default function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="bg-muted/30 border-t border-border py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p className="text-muted-foreground text-lg mb-4">
          © {currentYear} Ranjit Saroj. All rights reserved. | Safeguarding Digital Worlds
        </p>
        <p className="text-muted-foreground/80 flex items-center justify-center gap-2">
          <span>🛡️</span>
          Cybersecurity Professional | SOC Operations | Penetration Testing | Security Automation
        </p>
      </div>
    </footer>
  )
}
