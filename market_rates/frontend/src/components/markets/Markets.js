import React, { Component, Fragment } from 'react'
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getMarkets } from '../../actions/markets';

export class Markets extends Component {
    static PropTypes = {
        markets: PropTypes.array.isRequired
    };

    componentDidMount() {
        this.props.getMarkets();
    }

    render() {
        return (
            <Fragment>
                <h2> Lista de categorias </h2>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Nombre</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.markets.map(market => (
                            <tr key={market.id}>
                                <td> {market.id} </td>
                                <td> {market.name} </td>
                                <td> <button className="btn btn-danger btn-sm"> Borrar </button> </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </Fragment>
        );
    }
}
const mapStateToProps = (state) => ({
    markets: state.markets.markets
});

export default connect(mapStateToProps, { getMarkets })(Markets);
