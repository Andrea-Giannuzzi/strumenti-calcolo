"""
symbolic_derivatives.py

Breve guida eseguibile per calcolare derivate simboliche con SymPy,
fissando le variabili indipendenti e dichiarando esplicitamente la
dipendenza funzionale delle grandezze coinvolte.

Installazione dipendenza:
    python3 -m pip install sympy

Esecuzione:
    python3 symbolic_derivatives.py
"""

import sympy as sp


def print_section(title: str) -> None:
    """Stampa un titolo di sezione leggibile nel terminale."""
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def print_expression(description: str, expression: sp.Expr) -> None:
    """Stampa una descrizione e poi l'espressione in formato matematico."""
    print(f"\n{description}")
    print("-" * len(description))
    sp.pretty_print(expression)


def example_1_ordinary_derivatives() -> None:
    """Esempio 1: f = f(x), derivate ordinarie rispetto a x."""
    print_section("Esempio 1 - Derivate ordinarie di f = f(x)")

    # x e' la variabile indipendente.
    x = sp.symbols("x")

    # f_function e' una funzione simbolica non specificata.
    # f = f(x) dichiara esplicitamente che f dipende da x.
    f_function = sp.Function("f")
    f = f_function(x)

    df_dx = sp.diff(f, x)
    d2f_dx2 = sp.diff(f, x, 2)

    print_expression("Funzione dichiarata:", f)
    print_expression("df/dx:", df_dx)
    print_expression("d^2f/dx^2:", d2f_dx2)


def example_2_partial_derivatives() -> None:
    """Esempio 2: g = g(x, y), derivate parziali."""
    print_section("Esempio 2 - Derivate parziali di g = g(x, y)")

    # x e y sono variabili indipendenti.
    x, y = sp.symbols("x y")

    # g = g(x, y) dichiara che g dipende da entrambe le variabili.
    g_function = sp.Function("g")
    g = g_function(x, y)

    dg_dx = sp.diff(g, x)
    dg_dy = sp.diff(g, y)
    d2g_dxdy = sp.diff(g, x, y)

    print_expression("Funzione dichiarata:", g)
    print_expression("Derivata parziale dg/dx:", dg_dx)
    print_expression("Derivata parziale dg/dy:", dg_dy)
    print_expression("Derivata mista d^2g/(dx dy):", d2g_dxdy)


def example_3_chain_rule() -> None:
    """Esempio 3: V = V(q(t)), derivata totale rispetto a t."""
    print_section("Esempio 3 - Regola della catena per V = V(q(t))")

    # t e' la variabile indipendente.
    t = sp.symbols("t")

    # q = q(t) e' una funzione del tempo.
    q_function = sp.Function("q")
    q = q_function(t)

    # V = V(q(t)) dichiara che V dipende da q, e q dipende da t.
    V_function = sp.Function("V")
    V = V_function(q)

    # SymPy applica automaticamente la regola della catena:
    # dV/dt = (dV/dq) * (dq/dt).
    dV_dt = sp.diff(V, t)

    print_expression("Funzione composta dichiarata:", V)
    print_expression("dV/dt calcolata da SymPy:", dV_dt)


def example_4_euler_lagrange_terms() -> None:
    """Esempio 4: termini simbolici dell'equazione di Eulero-Lagrange."""
    print_section("Esempio 4 - L = L(q(t), dq/dt, t)")

    # t e' la variabile indipendente.
    t = sp.symbols("t")

    # q = q(t) e qdot = dq/dt sono le grandezze cinematiche.
    q_function = sp.Function("q")
    q = q_function(t)
    qdot = sp.diff(q, t)
    qddot = sp.diff(q, t, 2)

    # Q, Qdot e tau sono variabili ausiliarie indipendenti.
    # Servono per calcolare derivate parziali pulite di L(Q, Qdot, tau).
    Q, Qdot, tau = sp.symbols("Q Qdot tau")
    L_function = sp.Function("L")
    L_generic = L_function(Q, Qdot, tau)

    # Dopo avere calcolato le derivate parziali, sostituiamo:
    # Q -> q(t), Qdot -> dq/dt, tau -> t.
    substitutions = {Q: q, Qdot: qdot, tau: t}
    dL_dq = sp.diff(L_generic, Q).subs(substitutions)
    dL_dqdot = sp.diff(L_generic, Qdot).subs(substitutions)

    # Derivata totale rispetto al tempo di dL/dqdot.
    # Qui viene scritta esplicitamente la regola della catena:
    # d/dt A(Q, Qdot, tau) =
    #     dA/dQ * dq/dt + dA/dQdot * d2q/dt2 + dA/dtau,
    # dove A = dL/dQdot.
    A = sp.diff(L_generic, Qdot)
    d_dt_dL_dqdot = (
        sp.diff(A, Q).subs(substitutions) * qdot
        + sp.diff(A, Qdot).subs(substitutions) * qddot
        + sp.diff(A, tau).subs(substitutions)
    )

    euler_lagrange_left_side = sp.simplify(d_dt_dL_dqdot - dL_dq)
    euler_lagrange_equation = sp.Eq(euler_lagrange_left_side, 0)

    print_expression("Lagrangiana astratta:", L_generic.subs(substitutions))
    print_expression("qdot = dq/dt:", qdot)
    print_expression("Derivata parziale dL/dq:", dL_dq)
    print_expression("Derivata parziale dL/dqdot:", dL_dqdot)
    print_expression("Derivata totale d/dt(dL/dqdot):", d_dt_dL_dqdot)
    print_expression("Equazione di Eulero-Lagrange:", euler_lagrange_equation)


def main() -> None:
    """Esegue tutti gli esempi didattici."""
    sp.init_printing(use_unicode=True)

    print_section("Derivate simboliche con dipendenze funzionali esplicite")
    print(
        "Libreria usata: SymPy.\n"
        "Idea chiave: le variabili indipendenti si creano con symbols(), "
        "mentre le funzioni dipendenti si creano con Function()(variabili)."
    )

    example_1_ordinary_derivatives()
    example_2_partial_derivatives()
    example_3_chain_rule()
    example_4_euler_lagrange_terms()


if __name__ == "__main__":
    main()
