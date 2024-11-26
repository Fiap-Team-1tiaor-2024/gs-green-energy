import React, { useState, useEffect } from 'react';
import { AppBar, UserMenu, Logout } from 'react-admin';
import { TextField, Toolbar, Box } from '@mui/material';
import { fetchUtils } from 'react-admin';

const MyAppBar = (props) => {
    const [solar, setCampo1] = useState('');
    const [gas, setCampo2] = useState('');
    const [nuclear, setCampo3] = useState('');


    useEffect(() => {
        // Função assíncrona para buscar dados da API
        const fetchData = async () => {
            try {
                // Se você estiver usando o dataProvider do react-admin
                const httpClient = fetchUtils.fetchJson;
                const { json } = await httpClient('http://localhost:8000/api/tarifas');
                console.log(json[0].fonte.nome)
                // Supondo que a resposta da API seja um objeto com as chaves 'campo1', 'campo2', 'campo3'
                setCampo1(json[0].valor_tarifa);
                setCampo2(json[1].valor_tarifa);
                setCampo3(json[2].valor_tarifa);
            } catch (error) {
                console.error('Erro ao buscar dados da API:', error);
            }
        };

        fetchData();
        const interval = setInterval(fetchData, 5000);
        return () => clearInterval(interval);
    }, []);


    return (
        <AppBar {...props}>
            <Toolbar sx={{ width: '100%' }}>
                {/* Seus três TextFields */}
                <Box sx={{ flexGrow: 1, display: 'flex', alignItems: 'center' }}>
                    <TextField
                        label="Cotações"
                        variant="outlined"
                        size="small"
                        value=""
                        InputProps={{
                            readOnly: true,
                        }}
                        disabled
                        sx={{ mr: 2 }}
                    />
                    <TextField
                        label="Energia Solar"
                        variant="standard"
                        size="small"
                        value={solar}
                        InputProps={{
                            readOnly: true,
                        }}
                        disabled
                        sx={{ mr: 2 }}
                    />
                    <TextField
                        label="Gás"
                        variant="standard"
                        size="small"
                        value={gas}
                        InputProps={{
                            readOnly: true,
                        }}
                        disabled
                        sx={{ mr: 2 }}
                    />
                    <TextField
                        label="Energia nuclear"
                        variant="standard"
                        size="small"
                        value={nuclear}
                        InputProps={{
                            readOnly: true,
                        }}
                        disabled
                    />
                </Box>
                {/* UserMenu e outras ações */}
                <Box>
                    <UserMenu logout={<Logout />} />
                </Box>
            </Toolbar>
        </AppBar>
    );
};

export default MyAppBar;
