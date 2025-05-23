import React from 'react';
import styles from './HomePage.module.css';

function HomePage() {
  const currentYear = new Date().getFullYear();

  return (
    <div className={styles.container}>
      <section className={styles.hero}>
        <h1>OriEx: Tus Envíos de China a Argentina, Simplificados y Seguros.</h1>
        <p>
          Calcula tu envío, rastrea tu paquete y descubre la forma más confiable de
          conectar tus compras y negocios.
        </p>
        <div className={styles.heroButtons}>
          <button className={styles.primaryBtn}>Calcular Envío Ahora</button>
          <button className={styles.secondaryBtn}>Rastrear Paquete</button>
        </div>
      </section>

      <section className={styles.whyUs}>
        <h2>¿Por Qué Elegirnos?</h2>
        <ul className={styles.highlights}>
          <li>
            <span className={styles.icon}>💰</span>
            <p>Precios Competitivos</p>
          </li>
          <li>
            <span className={styles.icon}>📦</span>
            <p>Seguimiento en Tiempo Real</p>
          </li>
          <li>
            <span className={styles.icon}>🔍</span>
            <p>Proceso Transparente</p>
          </li>
          <li>
            <span className={styles.icon}>🤝</span>
            <p>Atención Personalizada</p>
          </li>
        </ul>
      </section>

      <section className={styles.howItWorks}>
        <h2>¿Cómo Funciona?</h2>
        <ol className={styles.steps}>
          <li>Cotiza y Registra</li>
          <li>Envía a nuestro Almacén en China</li>
          <li>Nosotros nos encargamos</li>
          <li>Recibe en Argentina</li>
        </ol>
      </section>

      <footer className={styles.footer}>
        <p>Copyright OriEx {currentYear}.</p>
        <div className={styles.footerLinks}>
          <a href="#">Términos y Condiciones</a>
          <a href="#">Política de Privacidad</a>
        </div>
      </footer>
    </div>
  );
}

export default HomePage;
